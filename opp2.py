class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print(f"My name is {self.name} I am {self.age} and a {self.gender}")

myob = Person("Charity Silah",17,"female")
myob.show()