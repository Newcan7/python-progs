import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('company_sales_data.csv')
plt.plot(df.month_number,df.total_profit)
plt.title('Company Title per month')
plt.xlabel('Month_Number')
plt.ylabel('Total_Profit')
plt.show()