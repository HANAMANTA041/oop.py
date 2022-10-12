
class Student:
    #"""Developed by Besant Tech for python demo"""
    def __init__(self):
        self.name = "Mary"
        self.age = 20
        self.marks = 80
   
    def talk (self):
        print("Hello I am :",self.name)
        print("My age is :",self.age)
        print("My marks are :",self.marks)
student_one = Student()
student_one.talk()
def talk(self):
        city = "Bangalore"
        print("city :",city)
def disp(self):
    print(city)
print(student_one.name)#instance variables are object level
#static or class vae common for all class
class Student:
    school_name = "Besant"
    def  __init__(self,name):
        self.name = name
    def disp(self):
        print("Student Name:",self.name)
"""

s1 = Student("Ramesh")
print(s1.name)
s1.disp()
s2 = Student("Suresh")
print(s1.school_name)
print(s2.school_name)
s1.school_name = "Besant HSR"
Student.school_name = "M HSR"#class level variable
print(s1.school_name)
print(s2.school_name)
print(Student.school_name)

class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("Hello my name is: ",self.name)
        print("My  rollno is: ",self.rollno)
        print("My marks are: ",self.marks)
student_one = Student("Mary",101,90)
student_one.talk()"""



    
        
