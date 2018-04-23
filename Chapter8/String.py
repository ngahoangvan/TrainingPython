prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter != 'Q' and letter != 'O':
        print(letter + suffix)

#Search
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('a3dasdbc', 'b'))

#Count
word = 'Pineapple'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)



if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')
