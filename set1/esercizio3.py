#esercizio 3
N=int(input("inserire lunghezza della lista: "))
for i in range(N):
  list[i]=input("inserire valore della lista: ")
if list[0]==list[N-1]:
 result=True
else:
 result=False
print(result)