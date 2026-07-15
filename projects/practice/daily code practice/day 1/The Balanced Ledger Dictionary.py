# 2. Title: The Balanced Ledger Dictionary
# Difficulty: Warm-up
# Topics Used: Dictionaries
# Problem Statement: Given a list of (person, amount) transactions where positive amounts are credits and negative are debits, build a dictionary showing each person's running balance, but only include people whose final balance is non-zero.
# Input: [("Ravi", 500), ("Meera", -200), ("Ravi", -500), ("Meera", 300)]
# Output: {"Meera": 100}
# Constraints: Names are case-sensitive. Amounts fit in standard int range.
# Logic Trigger: Ask yourself what should happen to an entry once its value hits zero.

# ---------------------------------------------------------------------------- #
#                                   Solution                                   #
# ---------------------------------------------------------------------------- #

# there is two way 
#1 

transactions =[
    ("ravi" , 500),
    ("meera" , -200), 
    ("ravi" , -500),
    ("meera" , 300)
]

balances = {}

for person , balance in transactions: 
    if person not in balances: 
        balances[person] = 0
         
    balances[person] += balance

result = {}

for person , balance in balances.items(): 
    if balance != 0 : 
        result[person] = balance

print(result)

#2
transactions =[
    ("ravi" , 500),
    ("meera" , -200), 
    ("ravi" , -500),
    ("meera" , 300)
]
balances = {}

for person , balance in transactions: 
    if person not in balances : 
        balances[person] = 0

    balances[person] += balance
     
    if balances[person] == 0 :
        del balances[person]

print(balances)