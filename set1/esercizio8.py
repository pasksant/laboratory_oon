def primo_mezzo_ultimo(string1,string2):
    lenght1=len(string1)
    lenght2=len(string2)
    string3 = string1(0) + string1(lenght1/2) + string1(lenght1)+ string2(0) + string2(lenght2/2) + string2(lenght2)
    return string3