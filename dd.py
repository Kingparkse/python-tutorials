class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def say_hello(self, to_name):
        print("안녕 "+ to_name + " 나는 " +self.name +" 이야")

park=Person("박", 20)
se = Person("세", 21)

park.say_hello("이")
se.say_hello("김")

class Police(Person):
    def po(self, to_po):
        print("너는 체포되됬다 "+to_po)
park = Police("세윤",20)
park.po("서령")

class Programmer(Person):
    def program(self,to_program):
        print("나는 만들어야겠다 "+to_program)
park = Programmer("세윤",27)
park.program("쿠버네티스")