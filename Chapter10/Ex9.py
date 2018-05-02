import time

f = open('word.txt')

def build_list1():
    word_list = []
    for line in f:
        word = line.strip()
        word_list.append(word)
    f.seek(0)
    return word_list

def build_list2():
    word_list = []
    for line in f:
        word = line.strip()
        word_list += [word]
    return word_list

start_time = time.time()
t = build_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = build_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')
