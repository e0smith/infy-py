#lex_auth_01269446319507046499

def remove_duplicates(value):
    value = ''.join(sorted(set(value), key=value.index))
    return value
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))