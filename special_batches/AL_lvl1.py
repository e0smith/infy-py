#lex_auth_012693797166096384149

def find_leap_years(given_year):
    list_of_leap_years=[]
        
    for count in range(1,16):
        if(((given_year%4==0) and given_year%100!=0) or given_year%400!=0):
            list_of_leap_years.append(given_year)
            given_year += 4
        else:
            given_year += 1
    return list_of_leap_years

list_of_leap_years=find_leap_years(200)
print(list_of_leap_years)