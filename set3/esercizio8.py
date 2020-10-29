import numpy as np
x=np.array([[34,43,73],[82,22,12],[53,94,66]])
y=np.array([10,10,10])
print(x)
w=np.delete(x,1,axis=1)
print(w)
z=np.insert(x,1,y,axis=1)
print(z)