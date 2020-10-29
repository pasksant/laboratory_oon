import numpy as np
x=np.array([[34,43,73],[82,22,12],[53,94,66]])
print(x)
num_element=np.prod(x.shape) #ritorna il numero di elementi
y=x.reshape(1,num_element)
print(y)
w=np.sort(y)
print(w)
z=w.reshape(3,3)
print(z)