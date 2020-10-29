import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales_data.csv')
total_profit=df['total_profit'].values
profit_range = [150e3,175e3,200e3,225e3,250e3,300e3,350e3]
plt.figure()
plt.hist(total_profit,profit_range,label='Month-wise Profit data of last year')
plt.xlabel('month number')
plt.ylabel('profit[$]')
plt.xticks(profit_range)
#plt.yticks([100e3,200e3,300e3,400e3,500e3])
plt.title('company profit per month')
plt.show()
