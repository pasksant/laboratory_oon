list1=[2,3,4,5,6,7,8]
list2=[4,9,16,25,36,49,64]
result = zip(list1,list2)
#other possibility
#result = [[a, b] for a in list1 for b in list2 if a != b]
result_set = set(result)
print(result_set)
