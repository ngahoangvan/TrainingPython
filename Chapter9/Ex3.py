def avoids(word, forb):
    for letter in forb:
        if letter in word:
            return False
    return True

#False
print(avoids("I'm the best! Ha Ha Ha!", 'abc'))

#True
print(avoids("I should study hard", 'egp'))

def no_contain(fin):
    forb = input('enter the forbidden letters: ')
    count = 0
    for word in fin:
        if avoids(word.strip(), forb):
            count += 1
    return count

fin = open('word.txt')
print ('the number of words:',no_contain(fin))
