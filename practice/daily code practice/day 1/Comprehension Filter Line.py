# 3. Title: The Comprehension Filter Line
# Difficulty: Warm-up
# Topics Used: List Comprehensions
# Problem Statement: Given a list of mixed-case words, produce a single list comprehension that returns only the words that start and end with the same letter (case-insensitive).
# Input: ["Eye", "Rotor", "Level", "Python", "Deed"]
# Output: ["Eye", Rotor", ""Level", "Deed"]
# Constraints: Words may include punctuation-free strings only. Single-letter words count as valid.
# Logic Trigger: Consider what part of a word never changes no matter how long it is.

# ---------------------------------------------------------------------------- #
#                                   solution                                   #
# ---------------------------------------------------------------------------- #

#without list comprehension : 
words = ["Eye", "Rotor", "Level", "Python", "Deed"]

result = []

for word in words: 
    if word[0].lower() == word[-1].lower(): 
        result.append(word)

print(result)

# with comprehension : 

words = ["Eye", "Rotor", "Level", "Python", "Deed"]

result = [
    word
    for word in words
    if word[0].lower() == word[-1].lower()
]
print(result)