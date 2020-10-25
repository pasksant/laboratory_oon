def conteggio(str):
     upper=0
     lower=0
     digits=0
     symb=0
for i in range(len(str)):
    if str[i].isupper():
      upper=upper + 1
    elif str[i].islower():
      lower= lower + 1
    elif str[i].isdigit():
      digits= digits + 1
    else:
      symb =symb + 1
    print('Upper case letters:', upper)
    print('Lower case letters:', lower)
    print('Number:', digits)
    print('Special characters:', symb)