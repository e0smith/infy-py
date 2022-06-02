#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    data1=data1.upper()
    data2=data2.upper()

    if(len(data1)!=len(data2) or (sorted(data1)!=sorted(data2))):
        return False
    
    for index in range(0, len(data1)):
        if(data1[index]==data2[index]):
            return False
    return True

print(check_anagram("eat","tea"))