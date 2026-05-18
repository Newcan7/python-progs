import numpy as np
a =np.random.randint(1,1000,(10,10))
print(a)
l=a[a>500]
print(l)
a[a %3 ==0] =50
print(a)
b=a[3:7,3:7]
print(b)
i =np.where(a%7 ==0)
print(i)