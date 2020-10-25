def coupled_element():
    firstList=[2,3,4,5,6,7,8]
    secondList=[4,9,16,25,36,49,64]
    thirdList = [[a, b] for a in firstList
              for b in secondList]
    print(thirdList)
