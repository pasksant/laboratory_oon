#esercizio 2
N=int(input("inserire lunghezza della lista: "))
prev=0
print("\nla somma del precedente e del successivo è: ")
for curr in range(N):
 if curr!=0:
  tot = prev+curr
  print("\n",tot)
 prev=curr