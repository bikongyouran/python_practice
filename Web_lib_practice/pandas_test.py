import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')
# print df.head()

plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
df.plot(ax=ax1)
plt.legend()
plt.show()