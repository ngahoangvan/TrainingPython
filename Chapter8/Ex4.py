#Wrong function
#Because it checking only firt character in String.
#If firt character is lowcase, it will be True, else it False.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#Wrong function
#This function is always return True because 'c'.islower() is True no what matter.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#Wrong function
#If last character is lowcase, it will be True, else it False.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

#Wrong function
#If c.islower() == true, flag will alway true. Because False or True => True.
#flag cannot be back false again.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#Right function
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

word = 'abCCbA'
print(any_lowercase1(word))
print(any_lowercase2(word))
print(any_lowercase3(word))
print(any_lowercase4(word))
print(any_lowercase5(word))
