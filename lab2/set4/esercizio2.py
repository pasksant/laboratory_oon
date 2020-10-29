import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data.csv')
total_profit=df['total_profit'].values
month_number=df['month_number'].values
print(total_profit,month_number)
plt.figure()
plt.plot(month_number,total_profit,label='Profit data of last year',color='r',marker='o',markerfacecolor='k',linestyle='--',linewidth=3)
plt.xlabel('month number')
plt.ylabel('profit[$]')
plt.legend(loc='lower right')
plt.xticks(month_number)
plt.yticks([100e3,200e3,300e3,400e3,500e3])
plt.title('company profit per month')
plt.show()