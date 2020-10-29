import numpy as np
x=np.array([[5,6,9],[21,18,27]])
y=np.array([[15,33,24],[4,7,1]])
z=x+y
print(z)
for element in np.nditer(z,op_flags=['readwrite']):
    element[...] = np.sqrt(element)
print(z)