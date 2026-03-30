# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(string):
    rev_digits = []
    for ch in reversed(string):
        if ch.isdigit():
            rev_digits.append(ch)
        else:
            break
    digits = rev_digits[::-1] 

    letters = []
    for ch in string[:len(string) - len(digits)]:
        letters.append(ch)
    letter = ''.join(letr for letr in letters)

    if (digits == []): return string+'1'

    if (int(''.join(digits)) != 0) : 
        num = int(''.join(digits)) + 1
        zeros = ''
        if ((len(string) - len(letter+str(num))) != 0):
            zeros = ['0' for n in range(len(string) - len(letter+str(num)))]
        return letter+''.join(zeros)+str(num)
    elif (len(digits) > 1):
        num = round(1 / 10 ** len(digits), len(digits))
        return letter+str(num)[2:]   


print(increment_string('foobar00'))