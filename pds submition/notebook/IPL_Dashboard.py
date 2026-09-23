"""
IPL MATCH ANALYTICS DASHBOARD
------------------------------
PBL Activity 4 - Case Study Analysis - Semester 5 (AI & Data Science)

Standalone dashboard script. Builds a single-figure analytics dashboard
from matches.csv and deliveries.csv using only Pandas, NumPy, Matplotlib,
and Seaborn (no Plotly, no ML model).

Usage:
    python IPL_Dashboard.py

Expects:
    ../data/matches.csv
    ../data/deliveries.csv

Produces:
    ../figures/dashboard.png

Every number shown on the dashboard is computed live from the CSV files
at run time. Nothing is hardcoded or assumed.
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

DATA_DIR = "../data"
FIGURES_DIR = "../figures"
MIN_MATCHES_TEAM = 20      # minimum matches for a team to qualify for the win% ranking
MIN_MATCHES_BAT = 10       # minimum matches for a batsman to qualify for runs-per-match ranking
MIN_BALLS_BOWL = 120       # minimum balls (20 overs) for a bowler to qualify for economy comparison

TEAM_NAME_MAP = {
    "Delhi Daredevils": "Delhi Capitals",
    "Deccan Chargers": "Sunrisers Hyderabad",
    "Kings XI Punjab": "Punjab Kings",
    "Rising Pune Supergiant": "Rising Pune Supergiants",
}


# ----------------------------------------------------------------------
# 1. DATA LOADING
# ----------------------------------------------------------------------
def load_data():
    """Load matches.csv and deliveries.csv. Fails loudly if missing."""
    matches_path = os.path.join(DATA_DIR, "/home/Leo/Documents/coding/ai/one_way/pds submition/data/matches.csv")
    deliveries_path = os.path.join(DATA_DIR, "/home/Leo/Documents/coding/ai/one_way/pds submition/data/deliveries.csv")

    if not os.path.exists(matches_path) or not os.path.exists(deliveries_path):
        sys.exit(
            f"ERROR: Expected 'matches.csv' and 'deliveries.csv' inside {DATA_DIR}/. "
            "Download the IPL dataset from Kaggle and place both files there, then re-run."
        )

    matches = pd.read_csv(matches_path)
    deliveries = pd.read_csv(deliveries_path)
    
    return matches, deliveries


# ----------------------------------------------------------------------
# 2. CLEANING (same logic as notebook Section 10, kept consistent)
# ----------------------------------------------------------------------
def clean_data(matches, deliveries):
    for col in ["team1", "team2", "toss_winner", "winner"]:
        if col in matches.columns:
            matches[col] = matches[col].replace(TEAM_NAME_MAP)
    for col in ["batting_team", "bowling_team"]:
        if col in deliveries.columns:
            deliveries[col] = deliveries[col].replace(TEAM_NAME_MAP)

    matches["winner"] = matches["winner"].fillna("No Result")
    matches = matches.drop_duplicates()
    deliveries = deliveries.drop_duplicates()
    matches["venue"] = matches["venue"].astype(str).str.strip()
    matches["date"] = pd.to_datetime(matches["date"], errors="coerce")

    return matches, deliveries


def prepare_data(matches, deliveries):
    deliveries_full = deliveries.merge(
        matches[["id", "season", "venue", "winner", "team1", "team2"]],
        left_on="match_id", right_on="id", how="left"
    )

    def classify_result(row):
        if row["winner"] == "No Result":
            return "No Result"
        if row.get("win_by_runs", 0) and row["win_by_runs"] > 0:
            return "Won batting first (by runs)"
        if row.get("win_by_wickets", 0) and row["win_by_wickets"] > 0:
            return "Won chasing (by wickets)"
        return "Other/Tie"

    matches["victory_type"] = matches.apply(classify_result, axis=1)
    matches["toss_winner_won_match"] = np.where(
        matches["toss_winner"] == matches["winner"], "Yes",
        np.where(matches["winner"] == "No Result", "No Result", "No")
    )
    return matches, deliveries_full


# ----------------------------------------------------------------------
# 3. METRIC COMPUTATION (mirrors notebook Sections 13-19)
# ----------------------------------------------------------------------
def compute_team_stats(matches):
    t1 = matches["team1"].value_counts()
    t2 = matches["team2"].value_counts()
    played = t1.add(t2, fill_value=0)
    wins = matches[matches["winner"] != "No Result"]["winner"].value_counts()

    team_stats = pd.DataFrame({"matches_played": played, "wins": wins}).fillna(0)
    team_stats["losses"] = team_stats["matches_played"] - team_stats["wins"]
    team_stats["win_pct"] = np.round((team_stats["wins"] / team_stats["matches_played"]) * 100, 2)
    team_stats = team_stats.sort_values("win_pct", ascending=False)

    qualified = team_stats[team_stats["matches_played"] >= MIN_MATCHES_TEAM]
    best_team_by_pct = qualified.sort_values("win_pct", ascending=False).head(10)
    return team_stats, best_team_by_pct


def compute_batting_stats(deliveries):
    batting = deliveries.groupby("batter").agg(
        total_runs=("batsman_runs", "sum"),
        balls_faced=("batsman_runs", "count"),
        matches_played=("match_id", "nunique"),
    ).reset_index()
    batting["runs_per_match"] = np.round(batting["total_runs"] / batting["matches_played"], 2)
    batting["strike_rate"] = np.round((batting["total_runs"] / batting["balls_faced"]) * 100, 2)
    top_run_scorers = batting.sort_values("total_runs", ascending=False).head(10)
    return batting, top_run_scorers


def compute_bowling_stats(deliveries):
    non_bowler_dismissals = ["run out", "retired hurt", "obstructing the field"]
    wickets = deliveries[
        (deliveries["is_wicket"] == 1) & (~deliveries["dismissal_kind"].isin(non_bowler_dismissals))
    ].groupby("bowler")["is_wicket"].sum()
    runs_conceded = deliveries.groupby("bowler")["total_runs"].sum()
    balls = deliveries.groupby("bowler")["ball"].count()
    matches_played = deliveries.groupby("bowler")["match_id"].nunique()

    bowling = pd.DataFrame({
        "wickets": wickets, "runs_conceded": runs_conceded,
        "balls_bowled": balls, "matches_played": matches_played
    }).fillna(0)
    bowling["economy"] = np.round(bowling["runs_conceded"] / (bowling["balls_bowled"] / 6), 2)
    top_wicket_takers = bowling.sort_values("wickets", ascending=False).head(10)
    return bowling, top_wicket_takers


def compute_venue_stats(matches):
    return matches["venue"].value_counts().head(10)


def compute_toss_and_probability(matches):
    toss_decision_counts = matches["toss_decision"].value_counts()
    valid = matches[matches["winner"] != "No Result"]
    toss_win_rate = (valid["toss_winner"] == valid["winner"]).mean() * 100

    bat_first_wins = (matches["victory_type"] == "Won batting first (by runs)").sum()
    chase_wins = (matches["victory_type"] == "Won chasing (by wickets)").sum()

    return toss_decision_counts, toss_win_rate, bat_first_wins, chase_wins


def compute_season_scoring_trend(deliveries_full):
    season_totals = deliveries_full.groupby(["season", "match_id"])["total_runs"].sum().reset_index()
    return season_totals.groupby("season")["total_runs"].mean().round(2)


# ----------------------------------------------------------------------
# 4. DASHBOARD RENDERING
# ----------------------------------------------------------------------
def build_dashboard(matches, deliveries, deliveries_full):
    team_stats, best_team_by_pct = compute_team_stats(matches)
    batting, top_run_scorers = compute_batting_stats(deliveries)
    bowling, top_wicket_takers = compute_bowling_stats(deliveries)
    venue_counts = compute_venue_stats(matches)
    toss_decision_counts, toss_win_rate, bat_first_wins, chase_wins = compute_toss_and_probability(matches)
    season_avg_runs = compute_season_scoring_trend(deliveries_full)
    total_decided = bat_first_wins + chase_wins

    kpi_total_matches = matches["id"].nunique()
    kpi_total_seasons = matches["season"].nunique()
    kpi_total_teams = len(pd.unique(matches[["team1", "team2"]].values.ravel()))
    kpi_total_venues = matches["venue"].nunique()
    kpi_best_team = best_team_by_pct.index[0] if len(best_team_by_pct) else "N/A"
    kpi_top_scorer = top_run_scorers.iloc[0]["batter"] if len(top_run_scorers) else "N/A"
    kpi_top_wicket_taker = top_wicket_takers.index[0] if len(top_wicket_takers) else "N/A"

    # ---- print KPI summary to console (for the report/viva to quote) ----
    print("IPL MATCH ANALYTICS DASHBOARD - KPI SUMMARY")
    print("-" * 45)
    print(f"Total Matches        : {kpi_total_matches}")
    print(f"Total Seasons        : {kpi_total_seasons}")
    print(f"Total Teams          : {kpi_total_teams}")
    print(f"Total Venues         : {kpi_total_venues}")
    print(f"Best Team (win %)    : {kpi_best_team}")
    print(f"Highest Run Scorer   : {kpi_top_scorer}")
    print(f"Highest Wicket Taker : {kpi_top_wicket_taker}")
    print(f"Toss winner won match: {np.round(toss_win_rate, 1)}% of decided matches")

    # ---- figure layout: 3x3 grid, 9 panels ----
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle("IPL MATCH ANALYTICS DASHBOARD", fontsize=18, fontweight="bold")
    gs = fig.add_gridspec(3, 3, hspace=0.6, wspace=0.35)

    # Panel 1 - Overview KPIs (Section 1 of dashboard spec)
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.axis("off")
    kpi_text = (
        f"Total Matches: {kpi_total_matches}\n"
        f"Total Seasons: {kpi_total_seasons}\n"
        f"Total Teams: {kpi_total_teams}\n"
        f"Total Venues: {kpi_total_venues}\n\n"
        f"Best Team: {kpi_best_team}\n"
        f"Top Scorer: {kpi_top_scorer}\n"
        f"Top Wicket-Taker: {kpi_top_wicket_taker}"
    )
    ax0.text(0, 1, kpi_text, fontsize=11, va="top")
    ax0.set_title("Overview KPIs", fontweight="bold")

    # Panel 2 - Team Performance (Section 2)
    ax1 = fig.add_subplot(gs[0, 1])
    if len(best_team_by_pct):
        best_team_by_pct["win_pct"].head(5).plot(kind="bar", ax=ax1, color="indianred")
    ax1.set_title(f"Top 5 Teams - Win % (min {MIN_MATCHES_TEAM} matches)")
    ax1.set_ylabel("Win %")
    ax1.tick_params(axis="x", rotation=60)

    # Panel 3 - Season scoring trend (Section 2 continued)
    ax2 = fig.add_subplot(gs[0, 2])
    season_avg_runs.plot(kind="line", marker="o", ax=ax2, color="brown")
    ax2.set_title("Avg Runs/Match by Season")
    ax2.set_ylabel("Avg Runs")
    ax2.tick_params(axis="x", rotation=60)

    # Panel 4 - Batting (Section 3)
    ax3 = fig.add_subplot(gs[1, 0])
    top_run_scorers.set_index("batter")["total_runs"].head(5).plot(kind="barh", ax=ax3, color="teal")
    ax3.invert_yaxis()
    ax3.set_title("Top 5 Run Scorers")
    ax3.set_xlabel("Total Runs")

    # Panel 5 - Bowling (Section 4)
    ax4 = fig.add_subplot(gs[1, 1])
    top_wicket_takers["wickets"].head(5).plot(kind="barh", ax=ax4, color="crimson")
    ax4.invert_yaxis()
    ax4.set_title("Top 5 Wicket Takers")
    ax4.set_xlabel("Wickets")

    # Panel 6 - Venue Analysis (Section 5)
    ax5 = fig.add_subplot(gs[1, 2])
    venue_counts.head(5).plot(kind="barh", ax=ax5, color="slateblue")
    ax5.invert_yaxis()
    ax5.set_title("Top 5 Venues (Matches Hosted)")
    ax5.set_xlabel("Matches")

    # Panel 7 - Toss (Section 6)
    ax6 = fig.add_subplot(gs[2, 0])
    toss_decision_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax6)
    ax6.set_ylabel("")
    ax6.set_title("Toss Decision Split")

    # Panel 8 - Bat first vs chase (Section 6 continued)
    ax7 = fig.add_subplot(gs[2, 1])
    if total_decided > 0:
        ax7.pie([bat_first_wins, chase_wins], labels=["Bat First", "Chase"],
                autopct="%1.1f%%", colors=["gold", "lightskyblue"])
    ax7.set_title("Bat First vs Chase Wins")

    # Panel 9 - Key Insights text (Section 7)
    ax8 = fig.add_subplot(gs[2, 2])
    ax8.axis("off")
    bat_first_pct = np.round(100 * bat_first_wins / total_decided, 1) if total_decided else 0
    chase_pct = np.round(100 * chase_wins / total_decided, 1) if total_decided else 0
    insights_text = (
        f"- Toss winner won match:\n  {np.round(toss_win_rate, 1)}% of decided matches\n"
        f"- Batting-first win share: {bat_first_pct}%\n"
        f"- Chasing win share: {chase_pct}%\n"
        f"- {kpi_total_teams} teams across\n  {kpi_total_seasons} seasons\n"
        f"- {kpi_total_venues} distinct venues used"
    )
    ax8.text(0, 1, insights_text, fontsize=10, va="top")
    ax8.set_title("Key Insights", fontweight="bold")

    os.makedirs(FIGURES_DIR, exist_ok=True)
    output_path = os.path.join(FIGURES_DIR, "dashboard.png")
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"\nDashboard saved to: {output_path}")
    plt.show()


# ----------------------------------------------------------------------
# 5. MAIN
# ----------------------------------------------------------------------
def main():
    matches, deliveries = load_data()
    matches, deliveries = clean_data(matches, deliveries)
    matches, deliveries_full = prepare_data(matches, deliveries)
    build_dashboard(matches, deliveries, deliveries_full)


if __name__ == "__main__":
    main()
