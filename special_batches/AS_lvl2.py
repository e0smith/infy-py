#lex_auth_012693816331657216161

def encode(message):
    
    total_count = 0
    count = 0
    result = ''
    space_holder = ''

    for x, y in zip(message, message[1:]):
        total_count += 1
        if ((x == y) and (total_count != (len(message)-1))):
            count += 1
            space_holder += x
            
        else:
            if total_count != (len(message)-1):
                count += 1
                add = str(count)
                result = result + add + x
                count = 0
            else:
                if ((len(space_holder) == 1 and x == space_holder[0]) or (x == space_holder[-1]) ):
                    count += 1
                    add = str(count)
                    result = result + add + x + '1' + message[-1]
                else:
                    result = result + '1' + x + '1' + message[-1]

    return result



#Provide different values for message and test your program
encoded_message=encode("ABCD")
print(encoded_message)