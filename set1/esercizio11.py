str='English = 78 Science = 83 Math = 68 History = 65'
sum=0
counts_num=0
words = str.split()
for num in words:
    if num.isnumeric():
       sum = sum + int(num)
       counts_num += 1
ave=sum/counts_num
print("la somma è",sum,"\nla media è",ave)



