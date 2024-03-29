# functions

# def hello():
#     print("hello World")
#
# hello()


# Parameters and Arguments

# def add(x, y):  # x , y parameters(while define)
#     print(x + y)
#
#
# a = int(input("Enter the first no : "))
# b = int(input("Enter the second no : "))

# add(a, b)  # a, b arguments(while calling)

# arbitrary arguments: access through index
# def hello(*name):
#     print("hello my name is", name[1])
#
# hello("john", "lisa", "peter")

# Return and recursion
# Return
# def hello():
#     return "hello world!"
#
#
# print(hello())

# Recursion

# def hello():
#     print("hello")
#     return hello()     #loop
#
# print(hello())

# factorial through recursion
# def facto(n):
#     if n == 1:
#         return 1
#     else:
#         return n * facto(n - 1)
#
#
# print(" the factorial of 5 is", facto(5))

# Lambda func

# x = lambda a,b,c : c*(a+b)
# print(x(10,20,30))

# Local and Global variables
# x = 24
# print(x)
#
# def xyz():
#     x = 25                 #local
#     return x
#
# print(xyz())
#
# print(x)

# x = 24
# print(x)
#
#
# def xyz():
#     global x  # global
#     return x
#
#
# print(xyz())
#
# print(x)





















