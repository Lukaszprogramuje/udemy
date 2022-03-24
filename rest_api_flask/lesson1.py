"""1"""

# x = 15

# price = 9.99

# discount = 0.2

# result = price * (1 - discount)
# print(result)

# name = "Luke"
# print(name)
# print(name * 2)

# a = 25
# b = a

# print(a)
# print(b)

# b = 15

# print(a)
# print(b)

"""2 fstring"""

# name = "Luke"
# # greeting = f"Hello, {name}"
# # print(greeting)

# # name = "Bob"
# # print(f"hello, {name}")

# greeting = "hello, {}"
# with_name = greeting.format(name)
# with_name_two = greeting.format("bob")
# print(with_name)
# print(with_name_two)

# longer_phrase = "hello, {}, today is {}"

# formatted = longer_phrase.format("Luke", "Monday")
# print(formatted)

"""3 user input"""

# name = input("enter your name")
# print(name)

# size = int(input("feet square"))
# square_meters = size / 10.8

# print(f"{square_meters:.2f}")

"""4 first app"""

# age = input("age")
# years = int(age)
# months = years * 12
# seconds = years * 365 * 24 * 60 * 60
# print(f"your age {years} this is monts {months} and this is {seconds} seconds")

"""5 list set tuples"""

# l = ["bob", "luke", "anna"] #modificate
# t = ("bob", "luke", "anna") #cant modificate
# s = {"bob", "luke", "anna", "tom"} #cant duplicate

# # l.append("tom")
# # l.remove("bob")
# # # print(t[0])
# # print(l)
# # print(s)
 
# set_2 = {"tom", "john"}

# local_friends = s.difference(set_2) 
# print(local_friends)

# total = s.union(set_2)
# print(total)

# both = s.intersection(set_2)
# print(both)

"""6 advanced set operation"""

# s = {"bob", "luke", "anna", "tom", "john"}
# set_2 = {"tom", "john"}
# print(s.difference(set_2))          # => set_2 = {'bob', 'anna', 'luke'}
# print(set_2.difference(s))          # => set()

# print(s.union(set_2)) #{'bob', 'john', 'anna', 'tom', 'luke'}

# print(s.intersection(set_2))  #{'john', 'tom'}
# print(set_2.intersection(s))    #{'john', 'tom'}

"""7 booleans"""

# print(5 == 5)
# print(5 != 5)           # ==, !=, >, <, >=, <=

# s = {"tom", "john"}
# set_2 = {"tom", "john"}

# print(s == set_2)
# print(s is set_2)

# s = set_2
# print(s is set_2)

"""8 if """

# a = 1
# if a == 1:
#     print("one")
# elif a == 2:
#     print("two")
# else:
#     print(a)

# b = input("number world ").lower()
# if b == "one":
#     print(1)
# else:
#     print(b)

"""9 in"""

# s = {"bob", "luke", "anna", "tom", "john"}

# print("bob" in s)

"""10 if with in"""

# s = {"bob", "luke", "anna", "tom", "john"}
# b = "bob"
# if b in s:
#     print("yes")
# else:
#     print("no")

# num = -1
# if num in (1, -1):
#     print("bravo")
# if abs(num) == 1:
#     print("bravo")

"""11 loops"""

# num = 1
# while num < 10:
#     print(num)
#     num +=1

# s = {"bob", "luke", "anna", "tom", "john"}
# for i in s:
#     print(f"{i} is my friend")

# grades = [30, 50, 20, 23]
# total = sum(grades)
# amount = len(grades)

# print(total/amount)