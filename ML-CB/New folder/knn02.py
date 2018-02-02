from jupyterthemes import jtplot
jtplot.style()
import numpy as np
from matplotlib import pyplot as plt

mean_01 = np.array([3.0,4.0])


#Lemons are sour, avg sweetness will low, they have some low value for color
# Red values is higher, Yellow Lower
# Sweetness is higher, Sourness Lower

cov_01 = np.array([[1.0,-0.5],[-0.5,1.0]])


mean_02 = np.array([0.0,-1.0])


cov_02 = np.array([[1,0.5],[0.5,0.6]])

dist_01 = np.random.multivariate_normal(mean_01,cov_01,200)
dist_02 = np.random.multivariate_normal(mean_02,cov_02,200)

#print dist_01.shape
#print dist_02.shape
#print dist_01


#scatter plot 
plt.figure(0)
for x in range(dist_01.shape[0]):
    plt.scatter(dist_01[x,0],dist_01[x,1],color='red')
    plt.scatter(dist_02[x,0],dist_02[x,1],color='blue')
#plt.show()


# Training Data Preparation

# 400 Samples - 200 Apples, 200 for Lemons

labels = np.zeros((400,1))
labels[200:] = 1.0

X_data = np.zeros((400,2))
X_data[:200,:] = dist_01
X_data[200: ,:] = dist_02

#print X_data
#print labels

#knn algorithm 

#Eucildean Distance
def dist(x1,x2):
    return np.sqrt(((x1-x2)**2).sum())

x1 =  np.array([0.0,0.0])
x2 =  np.array([1.0,1.0])

print dist(x1,x2)
