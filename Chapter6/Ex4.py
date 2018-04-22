def is_power(a, b):
    if a >= 1 and b >= 1:       
        if a < b  :  #Example: 3 is not power of 10
            return False
        if a == b:   #Example: 3 is power of 3
            return True
        else:
            return is_power(a / b, b)
    if 0 < b < 1:
        return False
    

print(is_power(9,3))