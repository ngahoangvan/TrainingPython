def count_of_a(words):
    count = 0
    for i in words:
        if i == 'a':
            count += 1
    return count

word = 'banana'

print(count_of_a(word))