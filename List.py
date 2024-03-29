list = ["Black Panther","Iron Man","Captain America","Thor"]
# print(list)
# print(list[::-1])  #rev
# print(list[::2])   #gap

# for i in list:
#     print(i)

# for i in range (len(list)):
#     print(list[i])

# List Comprehension

l1 = [30,40,50,60]

l2 = []

for i in l1:
    l2.append(i)

print(l1,"\n",l2)

l3 = [i for i in l1] #list comp
print(l3)

l3 = [i for i in l1 if i > 45] #list comp with filter
print(l3)