def sum_ave(str):
    sum=0
    j=0
    for i in range(len(str)):
        if str[i].isdigit():
           sum=sum+str[i]
           j=j+1
    ave=sum/j
    return sum
    return ave



