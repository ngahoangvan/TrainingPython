fin = open('words.txt')
word = fin.readlines()

def create_dict(word):
    a = dict()
    for c in word:
        for i in c:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
    return a

print(create_dict(word))