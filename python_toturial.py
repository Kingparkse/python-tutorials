# fruit 안에 있는 과일들의 종류와 갯수를 프린트 할 수 있는 함수(코드)를 작성 하시오.

fruit = ["사과", "사과",'바나나', '바나나', '딸기',"키워",'복숭아','복숭아','복숭아']

d = {} #dictionary 사용

for i in fruit: 
    if i in d: # 사과가 dict에 들어있니?
        d[i] = d[i] + 1 # 그럼 value를 +1 해줘
    else:
        d[i] = 1 #없으면 key를 추가하고 value를 1로 해줘 
print(d)