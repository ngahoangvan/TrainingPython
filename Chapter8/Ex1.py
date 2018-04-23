word = 'ABcXYzABcXYzABcXYz'

print(word.capitalize())
print(word.casefold())

a = word.endswith('AB',0,9) # Return the number
b = word.endswith('XYz',0,len(word))# Return true or false
c = word.find('Yz',0,len(word))
print(a)
print(b)
print(c)