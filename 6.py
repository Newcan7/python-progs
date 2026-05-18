import numpy as np
import pandas as pd
number=pd.Series(np.random.randint(1,1001,size=(100)))
l=[]
print(number)

for i in number:
    for j in range(2,i):
        if j%2==0:
        break
    l.append(i)
print(l)

        