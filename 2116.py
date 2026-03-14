#!/usr/bin/env python
# coding: utf-8

# In[101]:


import numpy as np
import matplotlib.pyplot as plt


# In[102]:


FILE = 'EXOPLANET ARCHIVE.csv'


# In[103]:


rough_data = np.genfromtxt(FILE, dtype='float', delimiter=',',skip_header=32)


# In[104]:


def is_valid(number):

    try:
        float(number)

        if np.abs(float(number)) >= 0:
            return True 
        return False 

    except ValueError:

        return False


# In[105]:


def read_text(rough_data):
    #radius:5 upper_unc:6 lower_unc:7
    #equ_temperature:13

    data = np.zeros((0, 4))
    for i in range(0, len(rough_data[:, 0])):
        if (is_valid(rough_data[i, 5]) and rough_data[i, 6] and is_valid(rough_data[i, 7]) and is_valid(rough_data[i,13])):
            temp = np.array([float(rough_data[i, 5]), float(rough_data[i, 6]), float(rough_data[i, 7]), float(rough_data[i, 13])])
            data = np.vstack((data, temp))
    return data


# In[106]:


def filter_text(rough_data):
    col_num=len(rough_data[0, :])
    data1 = np.zeros((0, col_num))
    data2 = np.zeros((0, col_num))
    for i in range(0, len(rough_data[:, 0])):
        if (rough_data[i, 0]<10 and rough_data[i, 1]>0.36):
            data1 = np.vstack((data1, rough_data[i, :]))
        else:
            data2 = np.vstack((data2, rough_data[i, :]))

    return data1, data2


# In[107]:


data=read_text(rough_data)
data1,data2=filter_text(data)


# In[108]:


print(data)
#radius\radius_upper unc\radius_lower unc\Tamperature effective


# In[109]:


print(data1)
#radius\radius_upper unc\radius_lower unc\Tamperature effective


# In[110]:


radius1=data1[:,0]
temper1=data1[:,3]
r_up_unc1=data1[:,1]
r_low_unc1=data1[:,2]


radius2=data2[:,0]
temper2=data2[:,3]

plt.scatter(temper2, radius2, color="blue", label="others")

plt.errorbar(temper1, radius1, 
             yerr=[np.abs(r_up_unc1), np.abs(r_low_unc1)], 
             fmt='o', alpha=0.6, color="red", label="hot juypter")



plt.title('f(x)')
plt.xlabel('Effective Temperature(K)')
plt.ylabel('Radius(Jupiter Radius)')
plt.legend()

plt.show()


# In[ ]:




