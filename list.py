# 리스트 []

# 짛하철 칸별로 10명 20명 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ['유재석', '조세호', '박명수']
# print(subway)

# #조세호가 타고있는 칸?
# print(subway.index('조세호'))

# # 하하가 다음 정류장에서 탔다
# subway.append('하하') # append는 맨뒤에 붙는다.
# print(subway)

# #정형돈을 유재석과 조세호 사이에 태운다
# subway.insert(1,'정형돈') #insert를 사용하여 넣고 싶은 순서에 배치한다.(순서, 넣을 객체)
# print(subway)

# # 지하철에 있는 사람을 한명씩 꺼냄
# # subway.pop()
# # print(subway.pop())

# # 같은 이름의 사람이 몇명인지 확인하기
# subway.append('유재석')
# print(subway)
# print(subway.count('유재석')) # count를 활용하여 같은 이름 몇명인지 찾기

# 정렬도 가능
# num_list=[5,2,4,1,3]
# num_list.sort()
# print(num_list)

# # 뒤집기
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형도 함께 사용가능
# num_list=[5,2,4,1,3]
# mix_list = ['조세호',20,True]
# #print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#사전

# cabinet = {3:'유재석', 100:'김태호'}
#print(cabinet[3])
#print(cabinet[100])

# print(cabinet.get(5))
# print(cabinet.get(5,"사용가능"))# .get 도 가능
# print("hi") # 키배정안된 숫자 프린트하면 오류나며 실행 종료됨

# print(3 in cabinet) #true
# print(5 in cabinet) #false

# cabinet = {"a-3":'유재석', "b-100":'김태호'}
# print(cabinet["a-3"])
# print(cabinet["b-100"])

# #새 손님
# print(cabinet)
# cabinet["a-3"] ="김종국"
# cabinet["c-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["a-3"]
# print(cabinet)

# #key 둘만 출력
# print(cabinet.keys())

# #value 둘만 출력
# print(cabinet.values())

# #key value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

#집합 (set)
# 중복안됨 순서없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java ={'유재석','김태호','양세형'}
# python = set(['유재석','박명수'])

# # 교집합 (java, python을 모두 할수 있는사람)
# print(java & python)
# print(java.intersection(python))

# #합집합(java도할수있거나 python할수있는 개발자)
# print(java | python)
# print(java.union(python))

# #차집합 (java 할수있지만 python 할수없는 개발자)
# print(java - python)
# print(java.difference(python))

# #python 할줄하는 사람이 늘어남
# python.add('김태호')
# print(python)

# #java를 잊었어요
# java.remove('김태호')
# print(java)

# # 자료구조의 변경
# menu = {'커피','우유','쥬스'}
# print(menu, type(menu))

# menu = list(menu)
# print(menu,type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu,  type(menu))

#quiz) 당신의 학교에 파이썬 코딩대회 주최
# 참여률을 높히기 위해 추첨을 통해 1명 치킨, 3명 커피쿠폰 받게된
# 추첨 프로그램 작성

# 조건 1 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2 댓글내영과 무관하게 무작위 추첨 중복 불가
# 조건 3 random 모듈의 shuffle 과 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 -- 
from random import *
users = range(1,21)
users = list(users)
shuffle(users)

winners = sample(users, 4) #4명중에 한명은 치킨 3명은 커피

print(' -- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print(' -- 축하합니다 --')