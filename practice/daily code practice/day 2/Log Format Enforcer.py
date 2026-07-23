# 6. Title: The Log Format Enforcer
# Difficulty: Core
# Topics Used: Regex, Functions
# Problem Statement: Write a function that checks whether each line in a list of server log strings matches a strict format: [YYYY-MM-DD HH:MM:SS] LEVEL: message, where LEVEL is one of INFO, WARNING, or ERROR. Return two separate lists — valid lines and malformed lines.
# Input: ["[2026-07-01 10:00:00] INFO: Server started", "2026-07-01 ERROR bad format", "[2026-07-01 10:05:12] CRITICAL: oops"]
# Output: valid = ["[2026-07-01 10:00:00] INFO: Server started"], invalid = [the other two]
# Constraints: Level matching must be exact — don't accept lowercase or unlisted levels.
# Logic Trigger: Consider building one pattern that captures every required piece at once, rather than checking pieces separately.


# ---------------------------------------------------------------------------- #
#                                    Answer                                    #
# ---------------------------------------------------------------------------- #

#^\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\]\s(INFO|WARNING|ERROR):\s.*$

import re

def check_logs(logs):

    pattern = r"^\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\]\s(INFO|WARNING|ERROR):\s.*$"

    valid = []
    invalid = []

    for line in logs:

        if re.match(pattern, line):
            valid.append(line)

        else:
            invalid.append(line)

    return valid, invalid

logs = [
    "[2026-07-01 10:00:00] INFO: Server started",
    "2026-07-01 ERROR bad format",
    "[2026-07-01 10:05:12] CRITICAL: oops"
]
valid, invalid = check_logs(logs)

print("Valid Logs")
print(valid)

print()

print("Invalid Logs")
print(invalid)