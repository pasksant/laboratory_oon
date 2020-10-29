list=[34,54,67,89,11,43,94]
print(list)
temp = list.pop(4)
print(list)
list.insert(2,temp)
list.append(temp)
print('the last versione of list is ',list)