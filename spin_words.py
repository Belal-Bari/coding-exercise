i = input("Give a sentence:\n")

def spin_words(sentence):
    temp = ''
    reverse = ''
    output = ''
    for letter in range(len(sentence)):                
        if i[letter].isalpha() or i[letter].isdigit() :
            temp += i[letter]
            if letter == len(sentence)-1:
                if len(temp) > 4:
                    for j in range(len(temp)-1, -1, -1):
                        reverse += temp[j]
                    temp = reverse
                    reverse = ''
                    output += temp
                    temp = ''
                else:
                    output += temp
                    temp = ''
        else:
            if len(temp) > 4:
                for j in range(len(temp)-1, -1, -1):
                    reverse += temp[j]
                output += reverse
                reverse = ''
                temp = ''

            temp += i[letter]
            output += temp
            temp = ''

        if letter == 0 or letter == len(sentence)-1:
            if i[letter] != '"':
                output += '"'

    print(output)
    return output

spin_words(i)