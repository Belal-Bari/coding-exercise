i = "Hey fellow warriors"

def spin_words(sentence):
    # Your code goes here
    temp = ''
    reverse = ''
    output = ''
    #print(temp)
    for letter in range(len(sentence)):
        #print(f"Iter {letter}")
        if letter > 0 and letter < len(i)-1:
            if i[letter] != ' ':
                temp += i[letter]
                #print("temp->", temp)
            else:
                if len(temp) > 4:
                    for j in range(len(temp)-1, -1, -1):
                        reverse += temp[j]
                    temp = reverse
                    reverse = ''

                    output += temp + ' '
                    temp = ''
                else:
                    output += temp + ' '
                    temp = ''
        elif letter == len(i)-1:
            temp += i[letter]
            #print("last", temp)
            output += temp
        else:
            temp += i[letter]
            #print("0->",temp)
    
    print(output)
    return output

spin_words(i)
