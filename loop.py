# LOOP

# n = int(input(" Enter the number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# with gap of 2
# for i in range(1,11, 2):
#     print(n, "x", i, "=", n*i)

# While loop

# n = 1
# a = 6
# while n <= 7:
#     print(a * n)
#     n += 1

# While True

# while True:
#     print("Hello")

# while True:
#     num1 = int(input("enter the 1st number"))
#     num2 = int(input("enter the 2nd number"))
#     print(num1 + num2)
#     choice = input("Do you want to continue ? ")
#     if choice == "no":
#         break

# Nested Loop
# pattern  problem

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
