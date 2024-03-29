# Application on Strings
a = "Sayan"
b = 'Sayan'
c = '''Sayan'''

print(a)
print(b)
print(c)

# Concatenation
Greeting = "Good Morning"
Name = " , Sayan"
print(Greeting + Name)

print(Greeting[0])

# Slicing n to n-1
print(Greeting[0:4])

# Skip

word = "amazing"
print(word[1:6:2])

# String function

story = '''Hello my name is Sayan ,
I have worked in Capgemini for 3 years"
as a SAP ABAP developer'''

print(story)
print(len(story))
print(story.count("i"))
print(story.find("Sayan"))
print(story.replace("developer", "Consultant"))
print(story.capitalize())  # makes the first character capital
# Escape sequence \n \t \ \\

