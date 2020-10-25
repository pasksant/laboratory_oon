def slice3_revert():
    list=[11,45,8,23,14,12,78,45,89]
    index=int(len(list)/3)
    list1=reversed(slice(index))
    list2=reversed(slice(index,2*index))
    list3=reversed(slice(2*index,len(list)))



