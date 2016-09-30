from matplotlib import pyplot as plt
import numpy as np
from io import BytesIO

fig = plt.figure()
t = np.arange(0,5,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
figData = BytesIO()
fig.savefig(figData, format='png')
figData.close()
