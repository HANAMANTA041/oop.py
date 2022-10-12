def tv_model (model,operation):
    print("TV model is :",model)
    print("TV operation is:",operation)
def fridge_model(model,operation):
    print("Fridge model is:",model)
    print("Fridge operation is:",operation)

tv_model("Samsung TV","Video")
fridge_model("BPL fridge","cooling")
tv_model("Videocon fridge","cooling")#data is not secure:it will not bound functions and variable .Therefore we go for class
fridge_model("Tv model xyz","Video")
class ClassName:
    def __init__(self):
        print("Constructer Called")#functions which are defined in class are called method
        print(id(self))

c_one = ClassName()
print(c_one)
print(id(c_one))
class TVModel:
    def __init__(self,model,operation):
        self.model = model#istance variables or attribute of object
        self.operation = operation
    def disp(self):
            print("Tv model",self.model)
            print("Tv operation",self.operation)
        
class FridgeModel:
    def __init__(self,model,operation):
        self.model = model
        self.operation = operation
    def disp(self):#instance method,self is not keyword,its convension,current object
            print("Fridge Model",self.model)
            print("Fridge operation",self.operation)

t_one = TVModel("Samsung 250","video")
f_one = FridgeModel("BPL Fridge","cooling")

t_one.disp()#instance method
f_one.disp()#object_name.method()
#class is binding attributes and methods is called encapsulation
#implementation details are hiding from the user=abstraction
class Student:
    """Developed by Besant Tech for python demo"""
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
        
