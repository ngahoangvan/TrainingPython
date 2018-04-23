def has_no_e(words):
    for letter in words:
        if letter == 'e':
            return False        
    return True

fin = open('word.txt')
word = fin.readlines()
# print(has_no_e(word))


def no_e(words):
    for letter in words:
        word = letter.strip()
        cout = 0
        for char in word:
            if has_no_e(char):
                print(char, end = '')
            else:
                cout += 1
                per = cout
    print ('\nPercent of e: ',per,'%')

no_e(word)
