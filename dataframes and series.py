import numpy as np
import pandas as pd
data = pd.read_csv("winemag-data-130k-v2.csv")
data=data.rename(columns={"country":"COUNTRY"})
print(data)
data["Index"]=np.arange(1,129972)
print(data)
cheap=data.loc[(data["COUNTRY"] == "Italy")  & (data["price"]>500)]
print(cheap)
cheap["COUNTRY"]=cheap["COUNTRY"]+"hello"
print(cheap)
print(data.groupby("COUNTRY")["points"].mean().sort_values())