import numpy as np
x=np.array([[34,43,73],[82,22,12],[53,94,66]])
print(x)
min_of_axis_0=np.amin(x,1) # (...,0) ritorna il minimo di ogni riga
max_of_axis_1=np.amax(x,0) # (...,1) ritorna il massimo di ogni colonna
print(min_of_axis_0,max_of_axis_1)
