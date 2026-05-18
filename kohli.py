import pandas as pd
runs = pd.read_csv("kohli_ipl.csv",index_col="match_no")
print(runs)
total=runs["runs"].sum()
print(total)