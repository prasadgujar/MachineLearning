from jupyterthemes import jtplot
jtplot.style()
import numpy as np
from matplotlib import pyplot as plt

mean_01 = np.array([3.0,4.0])


cov_01 = np.array([[1.0,0.5],[0.5,1.0]])

dist_01 = np.random.multivariate_normal(mean_01,cov_01,200)


print dist_01.shape
#print dist_01


#scatter plot 
plt.figure(0)
for x in range(dist_01.shape[0]):
    plt.scatter(dist_01[x,0],dist_01[x,1],color='red')
plt.show()
