"""14 list comprehensions"""

# numbers = [1, 3, 5]
# doubled =[x * 2 for x in numbers]


# s = {"abob", "aluke", "anna", "atom", "ajohn"}
# start = [friend for friend in s if friend.startswith("a") ]
# print(start)
# print(s)
# print(s is start)
# print(f" s {id(s)}   start {id(start)}")


"""15 Disctionares"""

# d = {"bob":24, "luke":27, "anna":35, "tom":44}
# print(d["bob"])

# a = [
#     {"name": "bob", "age": 24},
#     {"name": "anna", "age": 34},
#     {"name": "luke", "age": 25},
# ]

# print(a[1]["name"])

# d = {"bob":24, "luke":27, "anna":35, "tom":44}

# for x, y in d.items():
#     print(f"{x}: {y}")

# if "bob" in d:
#     print(f"bob: {d['bob']} ")       # ""and '' must use
# else:
#     print("no bob in dictionary")

# x = d.values()
# print(sum(x) / len(x))

"""16 desrtucturing variables"""

# t = 5, 11
# x, y = t
# print(x, y)
# d = {"bob":24, "luke":27, "anna":35, "tom":44}

# print(list(d.items()))              
# for x, y in d.items():          #destruction tuple
#     print(f"{x}: {y}")

# d = [("bob", 24, "mechanic"), ("luke", 27, "it"), ("anna", 35, "artist")]
# for name, age, profession in d:
#     print(f"{name}, {age}, {profession}")

# for person in d:
#     print(f"{person[0]}, {person[1]}, {person[2]}")

# person = ("bob", 24, "mechanic")
# name, _, profession  = person           # _ dont care, ignore this

# print(name, profession)

# head, *tail = [1, 2, 3, 4, 5]               # *all 
# print(head)
# print(tail)

# *head, tail = [1, 2, 3, 4, 5]               
# print(head)                                 #print with []
# print(tail)


# *head, tail = [1, 2, 3, 4, 5]               
# print(*head)                                # print without []
# print(tail)


"""17 function"""

def hello():
    print("hello")

hello()