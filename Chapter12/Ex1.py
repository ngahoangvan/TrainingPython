fin = open('words.txt')
line = fin.readlines()

def history(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] = i+1

    return d

h = history('line')
