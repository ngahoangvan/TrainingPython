def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that not work')

numA = input('Input number A: ')
numB = input('Input number B: ')
numC = input('Input number C: ')
numN = input('Input number D: ')

check_fermat(int(numA), int(numB), int(numC), int(numN))


