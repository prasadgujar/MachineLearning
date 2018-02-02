
# coding: utf-8

# In[5]:


from jupyterthemes import jtplot
jtplot.style()


a  =  np.asarray(range(100))

plt.figure(0)
plt.plot(a)

plt.figure(1)
plt.plot(a**2,color='green')
plt.plot(a**3,color='red')
plt.show()

