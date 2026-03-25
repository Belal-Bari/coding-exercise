# Write a function that takes a string input, and returns the first 
# character that is not repeated anywhere in the string.

# For example, if given the input "stress", the function should return 't', 
# since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase characters are considered 
# the same character, but the function should return the correct case for 
# the initial character. For example, the input "sTreSS" should return "T".

# If a string contains only repeating characters, return an empty string ("");

# Note: despite its name in some languages, your function should handle any Unicode codepoint:

# "@#@@*"    --> "#"
# "かか何"   --> "何"
# "🐐🦊🐐" --> "🦊"

def first_non_repeating_letter(s):
    if (s == '') : return ''
    ary = [letter.lower() for letter in s]
    print(ary)
    uniq_indx = [ary.index(letter) for letter in dict.fromkeys(ary) if ary.count(letter)==1]
    print(uniq_indx)
    if (uniq_indx == []) : return ''
    return s[uniq_indx[0]]

print(first_non_repeating_letter('sTreSS'))