sample_list=[11,45,8,23,14,12,78,45,89]
print("la lista di partenza è",sample_list)
chuck_size=int(len(sample_list)/3)
list1=list(reversed(sample_list[slice(0,chuck_size,1)]))
list2=list(reversed(sample_list[slice(chuck_size,2*chuck_size,1)]))
list3=list(reversed(sample_list[slice(2*chuck_size,3*chuck_size,1)]))
print('le tre liste ottenute sono: ')
print(list1)
print(list2)
print(list3)



