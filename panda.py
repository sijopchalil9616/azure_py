import pandas as pd
import numpy as np

# Creating empty series
ser = pd.Series()
print("Pandas Series: ", ser)

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
	
ser = pd.Series(data)
print("Pandas Series:\n", ser)



import pandas as pd
	
# Calling DataFrame constructor
df = pd.DataFrame()
print(df)

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
	
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)





import os

os.system("echo Hello from Sijo")