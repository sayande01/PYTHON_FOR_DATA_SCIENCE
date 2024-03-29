# Find length

a = "My name is Sayan De"
print("Length of the given string is ", len(a))
#
# # Find occurence
#
# print("The no of times a is coming", a.count("a"))
#
# # conversion lower/upper case
# x = a.lower()
# print(x)
# y = a.upper()
# print(y)
#
# #as title
# z =a.title()
# print(z)
#
# # find index no
# print(a.find("Sayan"))
#
# #capitalize the first letter
#
# #index of letter 'D'
#
# print(a.index("D"))

# format -> {}
# b = "My name is {}"
# print (b. format("Sandip"))

# case fold
# print(a.casefold())

# centralize
# b = "John"
# print(b.center(20,"*"))

# c = "hello"
# d = "hello123"
# e = "123456"
# f = "HELLO"
# g = " "
# h = "Hello 123"
# i = "1.234"
#
# # is alphanumeric isalnum()
#
# print(g.isalnum())
#
# # is Alphabet only isalpha()
# print(c.isalpha())
#
# #checks decimal only
# print(i.isdecimal())  # taking '.' as string dot "." not as a decimal point
#
# #check if only digits
# print(e.isdigit())
#
# #numeric check
# print(e.isnumeric())
#
# # check all letters if lowercase
# print(c.islower())
# print(f.isupper())
#
# # only space(white space) check
#
# print(h.isspace())
# print(g.isspace())
#
# # check if first letter of each word is in caps or not
# print(a.istitle())


a = "harry Potter"
print(a.endswith("r"))
print(a.startswith("h"))

b = "Lewis Hamilton"
print(b.swapcase())

c = "  ****** The  Goblin ......   "
print(c.strip("* , ."))

d = "#OOTD#BRB#ROFL#TBD"
print(d.split("#"))

e = "Sandra Bullock"

x = e.ljust(20)
y = e.rjust(20)
print(x)
print(y)

j = "John"
print(j.replace("John", "Lisa"))

r = "Lord of the rings"
print(r.index("rings"))


