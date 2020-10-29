import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data.csv')
facecream=df['facecream'].values
facewash=df['facewash'].values
toothpaste=df['toothpaste'].values
bathingsoap=df['bathingsoap'].values
shampoo=df['shampoo'].values
moisturizer=df['moisturizer'].values
month_number=df['month_number'].values
plt.figure()
plt.plot(month_number,facecream,label='facecream',marker='o',linewidth=3)
plt.plot(month_number,facewash,label='facewash',marker='o',linewidth=3)
plt.plot(month_number,toothpaste,label='toothpast',marker='o',linewidth=3)
plt.plot(month_number,bathingsoap,label='bathingsoap',marker='o',linewidth=3)
plt.plot(month_number,shampoo,label='shampoo',marker='o',linewidth=3)
plt.plot(month_number,moisturizer,label='moinsturizer',marker='o',linewidth=3)
plt.xlabel('month number')
plt.ylabel('products')
plt.legend(loc='upper left')
plt.xticks(month_number)
plt.yticks([1e3,2e3,4e3,6e3,8e3,10e3,12e3,15e3,18e3])
plt.grid(True,linewidth=0.5,linestyle='--')
plt.title('company product')
plt.savefig('sales_data_of_bathing_soap.png',dpi=150)
plt.show()
