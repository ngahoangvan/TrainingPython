def uses_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True

#False
print(uses_all('aeiou','aeiouy'))

#True
print(uses_all('aeiouy','aeiou'))