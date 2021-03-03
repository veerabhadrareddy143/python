import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts=pd.Series(np.random.randn(10))
ts=ts.cumsum()
columns=[1,2,3,4]
df=pd.DataFrame(np.random.randn(10,4),index=ts.index,columns=columns)
df=df.cumsum()
print(df)
#plt.plot(columns,ts)
df


