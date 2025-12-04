def to_camel_case(text):
    conv_up = False
    res = ''
    for letter in range(0,len(text)):
        if text[letter] in ['-', '_', ' ']:
            conv_up = True
        else:
            if conv_up == False:
                res = res + text[letter]
            else:
                res = res + text[letter].upper()
                conv_up = False
    return res