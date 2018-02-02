from jupyterthemes import jtplot
jtplot.style()
import numpy as np
from matplotlib import pyplot as plt

a  =  np.asarray(range(100))

plt.figure(0)
plt.plot(a)

plt.figure(1)
plt.plot(a**2,color='green')
plt.show()
