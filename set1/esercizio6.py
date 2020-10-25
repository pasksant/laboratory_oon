def conting(list1,list2):
    i=0
    j=0
    list3=[]
    for i in max(len(list1),len(list2)):
        if i<len(list1):
            if list1[i]%2!=0:
                list3[j]=list1[i]
                j += 1
        if i<len(list2):
           if list2[i]%2==0:
                list3[j]=list2[i]
                j += 1