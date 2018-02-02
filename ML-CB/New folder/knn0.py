

import numpy as np
from matplotlib import pyplot as plt

mean_01 = np.array([3.0,4.0])


cov_01 = np.array([[1.0,0.0],[0.0,1.0]])

dist_01 = np.random.multivariate_normal(mean_01,cov_01,200)


print dist_01.shape
print dist_01

