# class Person:
#     def __init__(self, name, age) -> None:
#         self.him = name
#         self.age = age

#     def walk(self):
#         print(self.him)

# Ore = Person('Ore', 24)
# Ore.walk()
# print(Ore.age)

#Inheritance
# class Animal:
#     def __init__(self, name, type) -> None:
#         self.animalName = name
#         self.animalType = type 

# class Dog(Animal):
#     def __init__(self, name, type) -> None:
#         super().__init__(name, type)

# class Bird(Animal):
#     def __init__(self, name, type) -> None:
#         super().__init__(name, type)

# puppy = Dog('Jack', 'german shepherd')
# print(puppy.animalName)        
# print(puppy.animalType)       



# class Human:
#     def __init__(self, name, height, age) -> None:
#         self.humanName = name
#         self.humanHeight = height
#         self.humanAge = age

# class Boy(Human):
#     def __init__(self, name, height, age) -> None:
#         super().__init__(name, height, age)

# class Girl(Human):
#     def __init__(self, name, height, age) -> None:
#         super().__init__(name, height, age)

# boy = Boy('Greg', 180, 17)
# girl = Girl('Esther', 170, 18)
# print(girl.humanName)                

# heirachy inheritance
class Mother:
    def __init__(self, name) -> None:
        self.Mname = name

class Father:
    def __init__(self, name) -> None:
        self.Fname = name     

class Child(Father, Mother):
    def __init__(self, name, Fname, Mname) -> None:
        self.cname = name
        super().__init__(Fname)
        Mother.__init__(self, Mname)

        self.child = name  
peter = Child('Peter', 'John', 'Mary')
# print(peter.Fname)
# print(peter.Mname)   
# print(peter.cname)     

# multilevel inheritance
class GrandParent:
    def __init__(self, name) -> None:
        self.gname = name

class Parent(GrandParent):
    def __init__(self, name, gname) -> None:
        super().__init__(gname)
        self.pname = name

class Child(Parent):
    def __init__(self, name, pname, gname) -> None:
        super().__init__(pname, gname)
        self.childname = name

boy = Child('Mark', 'Frank', 'Matt')
# print(boy.gname)        


# hybrid inheritance

class GreatParent:
    def __init__(self, greatma, greatpa) -> None:
        self.greatma = greatma
        self.greatpa = greatpa

class Father(GreatParent):
    def __init__(self, name, greatma, greatpa) -> None:
        GreatParent.__init__(self, greatma, greatpa)        
        self.pname = name

class Mother(GreatParent):
    def __init__(self, name, greatma, greatpa) -> None:
        GreatParent.__init__( self, greatma, greatpa)
        self.mname =  name

class Child(Father, Mother):
    def __init__(self, cname, pname, mname, greatma, greatpa) -> None:
         Father.__init__(self, pname, greatma, greatpa)
         Mother.__init__(self, mname, greatma, greatpa)
         self.child = cname

girl = Child('Esther', 'Mark', 'Mary', 'Lucy', 'John' )
# print(girl.pname)

# project
# create a class school 
# add a constructor that gets a list of 5 subjects
# add a method that displays all 5 subjects(get.subject)
# create a class person that inherits from school
# add a constructor that gets a name, age  and list of 5 subjects
# print the two things you like doing

class School:
    def __init__(self, subjects) -> None:
        self.subjects = subjects

    def getsubjects(self):
        print(f'these are my subjects: \n {self.subjects}')

class Person(School):
    def __init__(self, name, subjects, age, likes) -> None:
        super().__init__(subjects)
        self.name = name
        self.age = age
        self.likes = likes


mau = Person('Esther',["English", "math", 'history', 'socials', 'agric'], 20, ['reading', 'you'])
print(mau.likes)