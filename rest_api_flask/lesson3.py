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

users = [
    (0, "bob", "password"),
    (1, "john", "asdgasd"),
    (2, "mary", "aaa12345"),
    (3, "luke", "12345678")
]

username_mapping = {user[1]: user for user in users}

print(username_mapping["bob"])

username_input = input("enter name")
passowrd_input = input("enter password")

_, username, password = username_mapping[username_input]

if passowrd_input == password:
    print("correct")
else:
    print("wrong")




