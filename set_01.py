# Sets functions

# a = { "Sayan", "Sandip", "Suman", "Soumya", "Subho" }
# b = {"Antman", "Ben10" , "Batman"}
# c = { "Suman" , "Soumya"}
# d = { "Suman" , "Soumya" , "Kohli"}
#
# print(a) #unordered in every o/p
# print(type(a))

# Sets funcn

# add

# a.add("Spiderman")
# print(a)

# pop (randomly removes)
# a.pop()
# print(a)

# remove(speciific removal)
# a.remove("Sandip")
# print(a)

# discard
# a.discard("Sayan")
# print(a)

# copy

# b = a.copy()
# print(b)

# ==========================================

# isdisjont

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# issubset
# print(c.issubset(a))

# superset
# print(a.issuperset(c))

# update
# a.update(d)
# print(a)

# clear
# a.clear()
# print(a)

# ====================================================================

# a = { "Sayan", "Sandip", "Suman", "Soumya", "Subho" }
# b = {"Antman", "Ben10" , "Batman"}
# c = { "Suman" , "Soumya"}
# d = { "Suman" , "Soumya" , "Kohli"}

# Union
# print(a.union(b))

# Difference(discard ab common and b)(can be assigned in a different set)
# print(a.difference(c))

# difference updt

# a.difference_update(c)(within the same set)
# print(a)

# Intersection
# print(a.intersection(d))


# intersection update
# a.intersection_update(d)
# print(a)

# Symmetric difference(discard common values)

# x = a.symmetric_difference(d)
# print(x)

# Symmetric diff update
# a.symmetric_difference_update(d)
# print(a)

# ====================================== #

# a = [ 12, 56, 89 , 45, 47, 3, 96, 73 ]
# b = [ 56, 89 , 45, 101, 12,39, 10]
# c = [45, 91, 56 , 101, 10 ,7, 61 ]

# max = max(a)
# min = min(a)
#
# print(max)
# print(min)

# find common among 3 set
# print(set(a) & set(b) & set(c))

