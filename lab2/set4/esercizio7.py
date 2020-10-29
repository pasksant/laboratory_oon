import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data.csv')
months = df['month_number'].values
bathing_soap = df['bathingsoap'].values
face_wash_sales_data = df['facewash'].values
f,axs = plt.subplots(2, 1,sharex=True) #sono necessari sia f sia axs:f per chiamare la figura, axs per chiamare le sottofigure
#sharex per condividere i tick sull'asse comune in questo caso x
axs [0]. plot(months , bathing_soap , label='Bathing  soap  Sales Data',color='k', marker='o', linewidth =3)
axs [0]. set_title('Sales  data of a Bathing  soap')
axs [0]. grid(True , linewidth =0.5,  linestyle='--')
axs [0]. legend ()
axs [1]. plot(months , face_wash_sales_data , label='Face  Wash  Sales  Data',color='r', marker='o', linewidth =3)
axs [1]. set_title('Sales  data of a face  wash')
axs [1]. grid(True , linewidth =0.5,  linestyle='--')
axs [1]. legend ()
plt.xticks(months)
plt.xlabel('Month  Number')
plt.ylabel('Sales  units in  number')
plt.show()