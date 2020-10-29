set1={23,42,65,57,78,83,29}
set2={57,83,29,67,73,43,48}
intersection=set1.intersection(set2)
for item in intersection:
 set1.remove(item)
#an other possibility is
#set1 = [x for x in set1 if x not in set2]
print(set1)



