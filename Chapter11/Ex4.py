def has_duplicates(listOne):
   d = {}
   for item in listOne:
       d[item] = 1 + d.get(item, 0)
       if d[item] > 1:
           return True
   return False

t = ['a','b','c','d','a']

print(has_duplicates(t))

t[4] = 'e'
print(has_duplicates(t))