def is_triangle(a,b,c):
    if a + b > c and a + c > b and c + b > a:
        print('Yes')
    else:
        print('No')

numA = input('Enter number A: ')
numB = input('Enter number B: ')
numC = input('Enter number C: ')

is_triangle(int(numA), int(numB), int(numC))