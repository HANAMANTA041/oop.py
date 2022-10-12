"""
#1.Instance Methods
class Student:
    def __init__(self):
        self.a = 100

    def disp(self):
        a = 200
        print("The value of a is : ",self.a)
        print("The value of a is: ",a)
s = Student()
s.disp()


#decorater:adds more functionality,to identify class methods
#2.Class Methods
class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))

Animal.walk('Dog')
Animal.walk('Cat')


#3.Static Methods or utility methods
#static method = normal method
class CustomMath:
    
    @staticmethod
    def add(x,y):
        print("The Sum:",x+y)

   
    @staticmethod
    def product(x,y):
        print("The product:",x*y)
        
    @staticmethod
    def average(x,y):
        print("The average:",(x+y)/2)
CustomMath.add(10,20)
CustomMath.product(10,20)
CustomMath.average(10,20)

"""
#Use of super method
class P:
    a = 10
    def __init__(self):
        self.b = 10
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent static method")
class C(P):
    a = 888
    def __init__(self):
        self.b = 999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

c = C()


