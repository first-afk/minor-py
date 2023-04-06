# import random


class Students:
    def __init__(self, name, age, score) -> None:
        self.name = name
        self.age = age
        self.score = score

    def grade(self):
        if self.score < 30:
            return 'F'
        elif self.score < 40:
            return 'E'        
        elif self.score < 60:
            return 'C'    
        elif self.score < 70:
            return 'B'
        else:
            return 'A'        


f = open('myProject\\text.txt', 'r')
names = f.readlines()

from random import randrange
student = []
for name in names:
    student.append(Students(name.strip('\n'), randrange(16, 19), randrange(20, 100)))
    
for stud in student:
    print(f'Student name: {stud.name}; Student age: {stud.age}; Student score: {stud.score}; grade: {stud.grade()}')   