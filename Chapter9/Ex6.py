def is_abcedarian(word):
    i = 0
    while i < len(word) - 1:
        if word[i] > word[i + 1]:
            return False
        i = i + 1
    return True

# True
print(is_abcedarian('abcd'))
# False
print(is_abcedarian('dcba'))