class Person:
 def __init__(self, name): #생성자 : 클래스를 초기화하는 메소드	
  self.name = name 
  print("생성자 호출")

 def hello(self):
  print("하이!! " + self.name + "!")

 def goodbye(self):
  print("Good-bye " + self.name + "!")

p1 = Person("kim")
p1.hello()
p1.goodbye()