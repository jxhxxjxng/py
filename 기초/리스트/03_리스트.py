#리스트 = [데이터, 데이터, 데이터, ... , 데이터]

#리스트 생성하기
animals = ["사자", "호랑이", "고양이", "강아지"]

#데이터 접근하기
name = animals[3]

#데이터 추가하기
animals.append("하마")
animals.append(1)

#데이터 삭제하기
del animals[-1] # -1는 마지막 데이터

#리스트 슬라이싱
slicing = animals[1:3]

#리스트 길이
length = len(animals)

#리스트 정렬하기
animals.sort(reverse=True) #오름차순의 역순인 내림차순으로 정렬

print(animals)


