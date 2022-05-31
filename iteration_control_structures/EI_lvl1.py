#lex_auth_012693749623193600122

def find_sum_of_digits(number):
    sum_of_digits=0
    count = 0
    num = str(number)
    while count in range(len(num)):
        sum_of_digits = sum_of_digits + int(num[count])
        count += 1

    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)