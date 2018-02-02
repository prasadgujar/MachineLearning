import numpy as np
from matplotlib import pyplot as plt
#%matplotlib inline
arr  = np.array([1,2,3,4])

print type(arr)

#2-D arrays in Numpy
a = np.zeros((4,4))
print a

a[: , 0] = 2
a[1 , :] =  3
print a

#unique element
aa = np.asarray([1,2,3,5,3,4,2,1,7,7,7])

bb = np.unique(aa,return_counts=True)

print bb

index =  bb[1].argmax()

print bb[0][index]
