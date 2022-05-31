#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):

    common = ""
    
    for i in msg1.strip():
        if i in msg2.strip():
            common += i
            result = ''.join(sorted(set(common), key=common.index))
    if len(common) != 0:
        return result
    else:
        return -1

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)  