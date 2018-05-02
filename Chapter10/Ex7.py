def has_duplicates(list):
    t = list[:]
    t.sort()
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False
t = ['a','b','c','d','a']

print(has_duplicates(t))

t[4] = 'e'
print(has_duplicates(t))