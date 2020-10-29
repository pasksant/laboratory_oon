string1='OpenNets'
string2='Optical'
print("original string is ",string1+string2)
middleIndex = int(len(string1)/2)
string3= string1[:middleIndex] + string2 + string1[middleIndex:]
print("\nthe new string is", string3)