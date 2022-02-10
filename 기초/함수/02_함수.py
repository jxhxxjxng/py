def sum_all(start, end):
    변수 =0
    for i in range(start, end +1):
        변수 += i
    return 변수

print(sum_all(1,100)) 

def f(x):
    return x ** 2 + 1

print(f(10))     

def mul(*values):
    변수 = 1
    for i in values:
        변수 *= i
    return  변수

print(mul(5,7,9,10))