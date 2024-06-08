# functions  means set of instructions that can be executed in a program and can be called by name
# methods  means functions that belong to a class
# object oriented programming means that you can create your own classes and objects

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
    

Person1 = Person("John", 36)
Person1.myfunc()
