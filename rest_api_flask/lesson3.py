"""20 lambda functions"""

# add = lambda x, y: x + y

# print(add(5, 7))


# print((lambda x, y: x + y)(5, 7)


# def double(x):
#     return x * 2

# sequence = [1,3,5,7,9]
# doubled = [double(x) for x in sequence]

# doubled = map(double, sequence)                #map przejscie przez liste i zastosowanie funkcji

# doubled = [(lambda x: x * 2)(x) for x in sequence]
# doubled = list(map(lambda x: x * 2, sequence))
# print(doubled)


#                                   lambda to funkcje jednowierszowe bez nazwy

"""21 dictionary comprehension"""

# users = [
#     (0, "bob", "password"),
#     (1, "john", "asdgasd"),
#     (2, "mary", "aaa12345"),
#     (3, "luke", "12345678")
# ]

# username_mapping = {user[1]: user for user in users}

# print(username_mapping["bob"])

# username_input = input("enter name")
# passowrd_input = input("enter password")

# _, username, password = username_mapping[username_input]

# if passowrd_input == password:
#     print("correct")
# else:
#     print("wrong")

"""22 unpacking function arguments"""


# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total *= arg
#     return total

# print(multiply(4, 3, 5))



# def add(x, y):
#     print(f"x = {x}")
#     print(f"y = {y}")
#     return x + y

# nums = [4, 5]
# print(add(*nums))

# nums = {"y":10, "x":15}
# print(add(**nums))

# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total *= arg
#     return total

# def sum(args):
#     print(args)
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# def apply(*args, operator):
#     if operator == "*":
#         return multiply(*args)          #unpack and in function must use *
#     elif operator == "+":
#         return sum(args)
#     else:
#         return "no valid operator"

# print(apply(2, 4, 6, 7, operator="*"))
# print(apply(2, 4, 6, 7, operator="+"))

"""23 unpacking keywords arguments"""

# def named(name, age):
#     print(name, age)

# details = {"name": "bob", "age": "25"}
# named(**details)

# def named(**kwargs):
#     print(kwargs)

# def better(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# better(name = "bob", age=25)

# def both(*args, **kwargs):
#     print(args)
#     print(kwargs)

# both(1, 2, 3, 5, name = "bob", age = "25")

"""24 object oriented programming"""

# student = {"name": "bob", "grades": (33, 66, 56, 88, 99)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))

# class Student:
#     def __init__(self):
#         self.name = "bob"
#         self.grades = (33, 66, 56, 88, 99)

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)


# student = Student()
# print(student.name)
# print(student.grades)
# print(Student.average_grade(student))
# print(student.average_grade())                    #wywolanie na samym sobie

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)


# student = Student("bob", (33, 66, 56, 88, 99))
# student2 = Student("luke", (99, 88, 75, 44, 19))


# print(student2.name)
# print(student2.grades)
# print(student2.average_grade()) 

"""25 magic metod __str__ and __repr__"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old."  

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"
      

bob = Person("bob", 34)
print(bob)

