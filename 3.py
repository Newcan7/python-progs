import numpy as np
import pandas as pd
l= pd.Series([" alice ", "  BOB", "ChArLie ", "  david"])
cleaned_l=l.apply(lambda x: x.strip().title()).drop_duplicates()
print(cleaned_l)