class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def say_hello(self, to_name):
        print("안녕 "+ to_name+ " 나는 "+self.name)
        
    def introduce(self):
        print("내 이름은 "+self.name + "그리고 나는 "+str(self.age) + " 살이야")
se = Person("세윤",20)
seo = Person("서령","tl")

class Police(Person): #Person 상속
    def arrest(self,to_arrest):
        print("넌 체포됬다 "+to_arrest)
        
class Programmer(Person):
    def program(self,to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야 겠다 "+ to_program)
    
park = Person("세윤",20)
seo = Police("서령",21)
park1 = Programmer("세윤1",22)

park.introduce()
seo.introduce()
seo.arrest("세윤")
park1.introduce()
park1.program("이메일 클라이언트")