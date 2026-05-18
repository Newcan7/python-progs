import pandas as pd
import matplotlib.pyplot as plt
data = {'Category A' : 10, 'Category B' : 20, 'Category C' : 15, 'Category D' : 25}
series = pd.Series(data)
plt.bar(series.index, series.values, color = 'DarkGoldenRod')
plt.title('Customized Bar Chart with Matplotlib')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
ex=[]
for i in  series.values:
    if i==(max(series)):
        ex.append(0.3)
    else:
        ex.append(0)
plt.pie(series.values,explode=ex,shadow=True,labels=series.index)
plt.show()