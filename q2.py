import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Company_Sales.csv")
plt.plot(df["month_number"], df["total_profit"],linestyle=":", color="red", marker="o",markerfacecolor="red", linewidth=3, label="Profit")
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.title("Company Sales data of last year")
plt.legend(loc="lower right")
plt.show()