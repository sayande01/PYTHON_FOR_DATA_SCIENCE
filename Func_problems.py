# Maximum among the 3 numbers
# def maxima(a, b, c):
#     if a > b and a > c:
#         print("1st number is Largest")
#     elif b > c and b > a:
#         print("2nd number is Largest")
#     else:
#         print("3rd number is Largest")
#
#
# maxima(5, 14, 3)

# List to create ther squere of no between  1 and 30

# def create_list():
#
#     l = []
#     for i in range(1,31):
#         l.append((i**2))
#
#     return l
#
# print(create_list())

# check prime


# def check_prime(a):
#     if a == 1:
#         print("Not a prime")
#     if a == 2:
#         print("Its a prime")
#     if a > 2:
#         for i in range(2, a):
#             if a % i == 0:
#                 print("Not a prime")
#                 break
#         else:
#
#             print("Its a prime number")
#
#
# num = int(input("Enter the number: "))
# check_prime(num)

# funcn to find sum of n natural numbers

# def add(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#
#     print("total", total)
#
#
# num = int(input("Enter the nth number: "))
# add(num)


# Pass a list and get the esum
# def add(numbers):
#     total = 0
#     for i in numbers:
#         total = total + i
#     return total
#
#
# print(add([54, 24, 36, 47, 13]))

# Fibonacci using recursion

#
# def fibo(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return fibo(num - 1) + fibo(num - 2)
#
#
# print("The 7th term of the series is ",fibo(7))
