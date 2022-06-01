# aniaml package
# dog, cat modules
# dog, cat modules can say "hi"

#from animal import dog # animal 패키지에서 dog라는 모듈을 갖고와줘
#from animal import cat # animal 패키지에서 cat이라는 모듈을 갖고와줘

from animal import * # animal 패키지에서 갖고있는 모듈을 다 불러와

d = Dog() # instance
c = Cat()

d.hi()
c.hi()