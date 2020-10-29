sampleList=[87,52,44,53,54,87,52,53]
sampleList=list(set(sampleList)) #passaggio lista=>set=>lista ti permette di eliminare i duplicati
tup=tuple(sampleList)
min=min(tup)
max=max(tup)
print("la tupla è ",sampleList,"\ndi valore max",max,"\ndi valore min",min)
