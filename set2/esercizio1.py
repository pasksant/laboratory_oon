def even_odd():
    listThree=[]
    listOne = [3,6,9,12,15,18,21]
    listTwo = [4,8,12,16,20,24,28]
    for i in range(len(listOne)):
        if i%2==0:
            listThree[i]=listTwo[i]
        else:
            listThree[i]=listOne[i]


