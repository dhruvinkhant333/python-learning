# 1. Title: The Silent Vowel Counter
# Difficulty: Warm-up
# Topics Used: Strings, String Methods
# Problem Statement: Given a sentence, count how many vowels appear, but treat uppercase and lowercase the same, and ignore any vowels that are immediately repeated back-to-back (count a repeated run as one).
# Input: "Ede is reeeally eager"
# Output: 6
# Constraints: Input has only letters and spaces. Assume non-empty string.
# Logic Trigger: Think about what you need to remember from the previous character while scanning the current one.

sentence = input("Enter your sentense : ")

sentence = sentence.lower()

vowel = "aeiou"

count = 0

previous = ""

for ch in sentence : 
    if ch in vowel and ch != previous: 
        count +=1
    previous = ch

print(f"Vowel : {count}")


