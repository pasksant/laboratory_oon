dict1={'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'aug':44,'sept':54}
list1=[]
for item in dict1.values():
    if item not in list1:
        list1.append(item)
print(list1)