"""
HackerRank
TASK
----

You are given two classes, Person and Student, where Person is the base class and Student is the derived class. 
Completed code for Person and a declaration for Student are provided for you in the editor. 
Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
- A string, 'firstname'
- A string, 'lastname'
- An integer, 'id'
- An integer array (or vector) of test scores, 'scores'
A char calculate() method that calculates a Student object's average and returns the grade character 
representative of their calculated average:
'O' - 90 <= average <= 100
'E' - 80 <= average < 90
'A' - 70 <= average < 80
'P' - 55 <= average < 70
'D' - 40 <= average < 55
'T' - average < 40


Input Format
------------

The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. 
It also calls the calculate method which takes no arguments.

The first line contains , , and , separated by a space. 
The second line contains the number of test scores. 
The third line of space-separated integers describes .
"""


# BaseClass(parentClass)
class Person:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def printPerson(self):
        print(f"Name:{self.lastname},{self.firstname}\nID:{self.id}")



# DerivedClass(childClass)
class Student(Person):

    def __init__(self, firstname, lastname, idnum, scores):
        Person.firstname = firstname
        Person.lastname = lastname
        Person.id = idnum
        self.scores = scores

    def calc_avg(self):
        average = sum(self.scores)//len(self.scores)
        
        if average >= 90 and average <= 100:
            return 'O'
        elif average >= 80 and average < 90:
            return 'E'
        elif average >= 70 and average < 80:
            return 'A'
        elif average >= 55 and average < 70:
            return 'P'
        elif average >= 40 and average < 55:
            return 'D'
        else:
            return 'T'


data = input().split()
fname = data[0]
lname = data[1]
id = data[2]
scores = list(map(int, input().split()))

stud = Student(fname, lname, id, scores)
print(f"{stud.printPerson()}\nGrade:{stud.calc_avg()}")