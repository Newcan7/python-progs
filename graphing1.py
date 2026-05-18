import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
sales=pd.read_csv('company_sales_data.csv')
plt.plot(sales["month_number"],sales["total_profit"])
plt.title('company profit per month')
plt.xlabel('month number')
plt.ylabel('total profit')
plt.show()

plt.plot(sales["month_number"],sales["toothpaste"],'o')
plt.grid(linestyle="--")
plt.xlabel("Month Number")
plt.ylabel("Toothpaste")
plt.xticks(sales["month_number"])
plt.show()