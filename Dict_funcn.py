Bio = {"Name" : "Sayan", "Age": 26, "City" : "Kolkata"}

#get

# x = Bio.get("Name")
# print(x)
#
#
# # items(key value pairs
#
# a = Bio.items()
# print(a)
#
#
# # keys
#
# b= Bio.keys()
# print(b)
#
# # values
#
# c = Bio.values()
# print(c)
#
# # copy
#
# Bio2 = Bio.copy()
# print(Bio2)

# setdefault(resturns the value of the specified keyname

# x = Bio.setdefault("Age", 28)  #value is optional
# print(x)

# update

Bio.update({"Age" : 27})
print(Bio)

#adding items

Bio["Degree"] = "Btech"
print(Bio)

# remove item / pop

Bio.pop("City")
print(Bio)

# popitem = removes the last inserted item
Bio.popitem()
print(Bio)

#delete

del Bio["Age"]
print(Bio)

# clear - empties the dictionary

Bio.clear()
print(Bio)

