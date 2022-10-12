"""
#Duck Typing Philosophy in Python
class Duck:
    def talk(self):
        print("Quack Quack")
class Dog:
    def talk(self):
        print("Bow Bow")
class Cat:
    def talk(self):
        print("Meow Meow")
def obj_fun(obj):
    obj.talk()
d = Duck()
d.talk()
dg = Dog()
dg.talk()
c = Cat()
c.talk()

class Student:
    def walk(self):
        print("Student is walking")

s = Student()
s.walk()

#Overloading:same operator but multiple purposes Ex '+'
class Book:
    def __init__ (self,pages):
        self.pages = pages

    def __add__ (self,other):
        print("Id of b_one inside magic method is: ",id(self))
        print("Id of b_two inside magic method is: ",id(other))
        return self.pages+other.pages

b_one = Book(100)
b_two = Book(200)

b_three = b_one + b_two

print("Id of b_one is: ",id(b_one))
print("Id of b_two is: ",id(b_two))

print(b_three)


#Method overloading:Method overloading is , both method have same name, but different types 
#of arguments.
class Test:
    def m_one(self,arg):
        print("This is m_one method")
    def m_one(self,arg):
        print("This is m_one with arg")

t = Test()
t.m_one(5)


#Constructor Overloading

class Test:
    def __init__ (self):
        print("No arg constructor")
    def __init__ (self,arg):
        print("one arg constructor")
    def __init__(self,arg1,arg2):
        print("Two arg constructor")
t = Test(1, 2)


#Method overriding:A child class inherits all the methods from the parent class
#, the method inherited from the parent class doesn’t quite fit into the 
#child class. In such cases, you will have to re-implement method in the child class.

class Test:
    def __init__ (self,arg):
        print("No arg constructor")
        print("Value of arg is : ",arg)
class ChildTest(Test):
    def __init__(self,arg):
        super(). __init__ (arg)

t_child = ChildTest(90)



#Inheritance:
class P:
    a = 10
    def __init__ (self):
        self.b = 10

    def m1 (self):
        print("Parent instance method")

    @classmethod
    def m2 (cls):
        print("Parent class method")

    @staticmethod
    def m3():
        print("Parent static method")

class C(P):
    pass

c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()


#The concept of inheriting the properties from one class to another class is known 
#as single inheritance

class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")

c = C()
c.m1()
c.m2()

#The concept of inheriting the properties from multiple classes to single class with 
#the concept of one after another is known as multilevel inheritance

class P:
    def m1(self):
        print("Parent Method")
class C(P):
    def m2(self):
        print("Child Method")

class CC(C):
    def m3(self):
        print("Sub Child Method")

c = CC()
c.m1()
c.m2()
c.m3()


#The concept of inheriting properties from one class into multiple classes which 
#are present at same level is known as Hierarchical Inheritance
        
class P:
    def m1(self):
        print("Parent Method")

class C1(P):
    def m2(self):
        print("Child1 Method")

class C2(P):
    def m3(self):
        print("Child2 Method")

c1 = C1()
c1.m1()
c1.m2()
c2 = C2()
c2.m1()
c2.m3()

#The concept of inheriting the properties from multiple classes into a single class 
#at a time, is known as multiple inheritance.
class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m2(self):
        print("Parent2 Method")
class C(P1,P2):
    def m3(self):
        print("Child2 Method")

c =C()
c.m1()
c.m2()
c.m3()

class P1:
    def m1(self):
        print("Parent1 Method")
class P2:
    def m2(self):
        print("Parent2 Method")
class C(P2,P1):
    def m2(self):
        print("Child Method")

c = C()
c.m1()
c.m2()


#Method Resolution order(MRO)
#Working of MRO using python
class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")


r = B()
r.rk()

class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
#classes ordering
class D(C, B):
    pass

r = D()
r.rk()


#super() Method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print("Roll No:",self.rollno)
        print("Marks:",self.marks)

s1 = Student("Anil", 22, 101, 90)
s1.display()


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


#To call particular super class method
class A:
    def m1(self):
        print("A class Method")
class B(A):
    def m1(self):
        print("B class Method")
class C(B):
    def m1(self):
        print("C class Method")
class D(C):
    def m1(self):
        print("D class Method")
class E(D):
    def m1(self):
        A.m1(self)

e = E()
e.m1()

#Case-1
#Points about super
class P:
    a = 10
    def __init__(self):
        self.b = 20

class C(P):
    def m1(self):
        print(super().a)#valid
        print(self.b)#valid
        print(super().b)#invalid

c = C()
c.m1()

#Case-2
#Points about super
class P:
    def __init__(self):
        print("Parent Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("parent static method")

class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

c = C()
c.m1()


#Case-3
#points about super
class P:
    def __init__(self):
        print("Parent Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent static method")

class C(P):
    @classmethod
    def m1(cls):
        #super().__init__()--->valid
        #super().m1()___>invalid
        super().m2()
        super().m3()

C.m1()


#From Class Method of Child class, how to call parent class instance 
#methods and constructors:
class A:
    def __init__(self):
        print("Parent constructor")
    def m1(self):
        print("Parent instance method")

class B(A):
    @classmethod
    def m2(cls):
        super(B,cls).__init__(cls)
        super(B,cls).m1(cls)

B.m2()
"""
"""
#Case-4 In child class static method we are not allowed to use super()generally
class P:
    def __init__(self):
        print("Parent Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent static method")

class C(P):
    @staticmethod
    def m1():
        super().m1()#invalid
        super().m2()#invalid
        super().m3()#invalid

C.m1()
"""
#output
"""
Traceback (most recent call last):
  File "D:\pythoncodes\ooppoly.py", line 414, in <module>
    C.m1()
  File "D:\pythoncodes\ooppoly.py", line 410, in m1
    super().m1()#invalid
RuntimeError: super(): no arguments
"""

#How to call parent class static method from child class static method by using 
#super()
class A:
    @staticmethod
    def m1():
        print("Parent static method")
class B(A):
    @staticmethod
    def m2():
        super (B,B).m1()
B.m2()




            
        

    

