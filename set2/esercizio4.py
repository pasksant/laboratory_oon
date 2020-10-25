def cont_occurences():
    list=[11,45,8,11,23,45,23,45,89]
    i=0
    j=0
    for i in range(enumerate(list)):
     count=0
     for j in range(enumerate(list)):
        if list(i)==list(j):
         count=count +1
     print("/n",count)
     dict[i] = count
