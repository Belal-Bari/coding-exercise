# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

# Test examples:

# "EBG13 rknzcyr." -> "ROT13 example."

# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

def rot13(message):
    decoded = []
    for c in message:
        if (64 < ord(c) and ord(c) < 91) :
            pos = ord(c) - 64
            diff = 26 - pos
            if(13 > diff):
                shift_pos = 13 - diff
                decoded.append(chr(shift_pos+64))
            else:
                shift_pos = 13 + pos
                decoded.append(chr(shift_pos+64))
        elif (96 < ord(c) and ord(c) < 123):
            pos = ord(c) - 96
            diff = 26 - pos
            if(13 > diff):
                shift_pos = 13 - diff
                decoded.append(chr(shift_pos+96))
            else:
                shift_pos = 13 + pos
                decoded.append(chr(shift_pos+96))
        else:
            decoded.append(c)
    return ''.join(decoded)

print(rot13("EBG13 rknzcyr."))
print(rot13("Guvf vf zl svefg EBG13 rkprepvfr!"))