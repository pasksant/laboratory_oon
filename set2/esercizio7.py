def one_inside_other():
    firstSet={57,83,29}
    secondSet={57,83,29,67,73,43,48}
    sub=firstSet.issubset(secondSet)
    sup=firstSet.issuperset(secondSet)
    if sub==1:
        print("firstSet is a subset of secondSet")
        firstSet = [x for x in firstSet if x not in secondSet]
    elif sup==1:
        print("secondSet is superset of SecondSet")
        secondSet = [x for x in secondSet if x not in firstSet]
    else:
        print("non ci sono subset")
