import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Company_Sales.csv")

plt.plot(df["month_number"], df["total_profit"])
plt.xlabel("Month Number")
plt.ylabel("Total profit")
plt.title("Company profit per month")
plt.show()