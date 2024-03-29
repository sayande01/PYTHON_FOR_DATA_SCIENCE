a = ("HP", "Lenovo", "Dell" , "MSI", "Alenware", "Asus")
print(type(a))
a = list(a)  #tuple converting to list
print(type(a))

a.append("Vivobook")
a = tuple(a)    #list => tuple
print(a)

print(a.count("Lenovo"))  #occurence count
print(a.index("MSI"))     #index find


