list=[11,45,8,11,23,45,23,45,89]
dict1=dict()
for element in list:
 count=0
 for el in list:
  if el==element:
    count=count+1
 dict1[element] = count
print(dict1)
