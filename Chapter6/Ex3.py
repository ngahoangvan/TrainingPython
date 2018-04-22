def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

#No output
print(middle('ab'))
print(middle('a'))
print(middle(''))

#TypeError: 'int' object is not subscriptable
#print(middle(1))


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('abccba'))
print(is_palindrome('redivider'))
print(is_palindrome('abcde'))
