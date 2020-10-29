string1='America'
string2='Japan'
string3 = string1[0] + string1[int(len(string2)/2)] + string1[int(len(string1))-1] + string2[0] + string2[int(len(string2)/2)] + string2[int(len(string2))-1]
print("the new string is",string3)