#-----------EX1---------

def right_justify(text):
    
    print(text * (70 // len('monty')))

right_justify('monty')

#-----------EX2---------
#-----------1---------

# def do_twice(f):
#     f()
#     f()

# def print_spam():
#     print('spam')

# do_twice(print_spam)

#-----------2---------

def do_twice(f, value):
    f(value)
    f(value)

def print_spam(value):
    print(value)

do_twice(print_spam, 12)

#-----------3 and 4---------

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice,'spam')

#-----------5---------

def do_four(value):
    do_twice(print_spam, value)
    do_twice(print_spam, value)

do_four('Hello Python')


