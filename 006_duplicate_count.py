# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters 
# and numeric digits that occur more than once in the input string. The input string can be assumed 
# to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    seen = []
    for letter in range(0,len(text)-1):
        if text[letter].lower() in text[letter+1:].lower() and text[letter].lower() not in seen:
            seen.append(text[letter].lower())
    return len(seen)

duplicate_count('aabBcde')