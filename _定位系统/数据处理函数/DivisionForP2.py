#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from sklearn.utils import shuffle


# In[12]:


#该方法用于引入数据集，数据集要求为已经向量化的数据
#输入为文件名，默认在/Data文件夹中，数据形式为【区域，x，y，样本】
#返回为labels，samples，同索引的对应
def Dataset(Filename):
    datas = pd.read_csv("./Data/"+Filename,header=None)
    datas = np.array(datas)
    labels = datas[:,:3]    # csv数据中，前三列为label：区域，x，y
    samples = datas[:,3:]   # 之后的为样本
    return labels,samples


# In[13]:


#该方法用于为第二阶段打乱拆分数据集，会使用Dataset方法
#输入为文件名，默认在/Data文件夹中数据形式为【区域，x，y，样本】
#输出为train的x，y；test的x，y
#由于采样基本是均匀每个点采到5次，所以拆分测试用数据为5次中随机一次，每个点均取
#因此该函数并不是完全随机抽出百分之20，这点需要留意
def DivisionP2(Filename):
    labels,samples = Dataset(Filename)
    x,y = shuffle(samples,labels)   # 打乱数据
    # 由于打乱了数据，因此取每个（区域，x，y）出现的第一个，也具有随机特性。
    test = []    # 用于存放取出数据的索引
    for area in range(1,33):      # 针对每一个区域，由于至多为32
        for i in range(1,6):      # 针对每一个x坐标,由于至多为5
            for j in range(1,6):   # 针对每一个y坐标
                for k in range(len(y)):  # 末级循环：遍历所有样本
                    if y[k][0]==area and y[k][1]==i and y[k][2]==j:  #如果首次出现符合的
                        test.append(k)    # 取出索引
                        break       # 跳出末级循环，意味着只取同条件的第一个样本
    test_x = x[test]     # 按索引存放test的x
    test_y = y[test]     # 按索引存放test的y
    train_x = np.delete(x,test,0)  # 取出索引为test的数据存入train
    train_y = np.delete(y,test,0)  # 取出索引为test的数据存入train
    return train_x,train_y,test_x,test_y


# In[14]:





# In[7]:





# In[8]:





# In[9]:





# In[64]:





# In[65]:





# In[66]:





# In[ ]:




