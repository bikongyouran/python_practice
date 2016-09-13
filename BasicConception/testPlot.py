from matplotlib import pyplot as plt
import pandas as pd

def func(x):
    if x == True:
        return 1
    else:
        return 0


df = pd.read_csv('test.csv')

# df2 = df[['DocType','HasOCRAddress']]
df2 = df.loc[:,('DocType','HasOCRAddress')]

df2['test'] = df2['HasOCRAddress'].apply(func)
df3 = df2.loc[:,('DocType','test')]
print df3
df3.apply(pd.value_counts).plot(kind='bar')
plt.show()

