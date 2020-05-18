class Things:
    pass

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("My name is {0} and my age is {1}".format(self.name,self.age))

p1 = Person("Amit",43)
p1.age = 33
p1.myfunc()
#del p1.age
#del p1
