import math

def mysqrt(a, epsilon=0.0000001 ):
    # Initial guess also coerces `a` to a float
    x = a / 2.0
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

def printSqrt(a):
    while (a <= 9) :
        test_square_root(a)
        a = a + 1

def test_square_root(a):
    print(a, mysqrt(a), math.sqrt(a), math.sqrt(a) - mysqrt(a))
    
print('a    mysqrt(a)   math.sqrt(a)    diff')
print('-    ---------   ------------    ----')

printSqrt(1)


