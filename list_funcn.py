
list = ["Black Panther","Iron Man","Captain America","Thor"]
print(len(list))
print(list.count("thor"))

list.append("Gekko")
list.insert(1,"Vision")
list.remove("Thor")

print(list)
print(list.pop(2))  #remove list object using index
print(list)


# copy of a list

b = []
b = list.copy()
print(b)

#extend a list
c = [ "Wingman", "Reyna"]
list.extend(c)
print(list)

#reverse a list
list.reverse()
print(list)

#ascending order sort
list.sort()
print(list)

# clear data from list

list.clear()
print(list)

