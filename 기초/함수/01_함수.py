# def 함수이름(매개변수):
#     명령블록
    
#     return 리턴값

import random


def sum(a,b):
    result = a + b
    return result

x = sum(1,2)
y = sum(3,4)
print(x)

#매개변수가 없는 함수
# def 함수이름():
#     명령블록
    
#     return 리턴값

def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())

#매개변수만 있고 return값이 없는 함수
def printName(name):
    print(name)

#매개변수가 없고 return도 없는 함수
def sayHi():
    print("안녕하세요")