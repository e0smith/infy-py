#lex_auth_012693750719488000124

def get_count(num_list):
    count=0

    # Write your logic here

    for x, y in zip(num_list, num_list[1:]):
        if x == y:
            count +=1
        

    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
