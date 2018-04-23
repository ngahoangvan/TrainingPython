fruit = 'banana'
print(fruit[0:5:2])

def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome('abccba'))
print(is_palindrome('redivider'))
print(is_palindrome('abcde'))
