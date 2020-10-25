def in_the_middle(string1,string2):
    middleIndex = int(len(string1)/2)
    stringA=string1[:middleIndex]
    stringB=string1[middleIndex:]
    string3= stringA + string2 +stringB
    return string3