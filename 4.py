import numpy as np
m= np.random.randint(1,101,size=(10,10))
print(m)
print(m[3:6,3:6])
fifty = m[m>50].tolist()
m[m>50]=0
m[m%3]=-1


print(m)
print(fifty)