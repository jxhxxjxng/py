from tkinter import N


#n! = 1 * 2 *3 *... * (n-1) * N

def factorial_1(n):
    변수 = 1
    for i in range (1, n + 1):
        변수 *= i
    return 변수

print(factorial_1(4))

#n! = n * (n-1)!

def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n-1)
    
print(factorial_2(4))