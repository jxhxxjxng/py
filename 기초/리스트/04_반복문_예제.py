from re import I


num = int(input("자연수를 입력해 주세요"))

sum = 0
for i in range(1, num + 1):
    sum = sum + i
    
print(sum)