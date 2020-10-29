list1=[10,20,23,11,17]
list2=[13,43,24,36,12]
i=0
j=0
list3=[]
for element in list1:
    if element%2!=0:
        list3.append(element)
for element in list2:
    if element%2==0:
        list3.append(element)
for element in list3:
    print("the merged list is",element)
