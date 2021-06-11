#!/usr/bin/env python
# coding: utf-8

# In[76]:


import csv
from collections import Counter
import numpy as np


# In[2]:


#这个函数用语删除部分出现问题的行
#输入为文件名，默认放在/Data中
#输出为文件，前缀加上Del_
#该输出文件的含义是，初步去除无效行的数据集
#主要实现了删除读不到rssi的行。这些行可能由于AP名称中有中文导致采集时乱码所致
def DeleteErrorRow(FileName):
    with open("./Data/"+FileName,'r',encoding='iso-8859-1') as inp,    open("./Data/Del_"+FileName,'w',encoding='iso-8859-1',newline='') as out:
        rd = csv.reader(inp)
        wt = csv.writer(out)
        for row in rd:
            if row[8] != '':    # 如果RSSI为空，这可能是由于采集时出现了乱码
                print(row)
                wt.writerow(row)


# In[40]:


#这个函数用于统计数据集中AP的个数
#输入为文件名，默认在/Data中
#输出为文件，前缀加上ApList_
#该输出文件的含义是，数据集文件中出现的所有AP，及其次数统计
def ApList(FileName):
    ListAll = []
    with open("./Data/"+FileName,'r',encoding='iso-8859-1') as inp,    open("./Data/ApList_"+FileName,'w',encoding='iso-8859-1',newline='') as out:
        rd = csv.reader(inp)
        wt = csv.writer(out)
        for row in rd:
            ListAll.append(row[7])  # 记录所有条目的Mac地址
        aplist = Counter(ListAll)   # 挑出不同的Mac并计数每个Mac出现的次数
        # 调试记录，数据集1共有521条AP；2共有681条
        for ap in aplist.items():
            print(ap)
            wt.writerow(ap)


# In[68]:


#这个函数用于求得两个数据集中共同出现的AP
#输入是两个数据集的APlist文件名，这个文件由Aplist函数求得
#输出是一个文件，命名后缀带All
#文件内容是，两个数据集中共同出现的AP，及其在0，1两个数据集中出现的次数
def Intersection(List0,List1):
    aplist0 = []  # 记录数据集0的aplist
    count0 = []
    aplist1 = []  # 记录数据集1的aplist
    count1 = []
    aplist = []   #需要输出的交集结果列表
    with open("./Data/"+List0,'r',encoding='iso-8859-1') as inp0,    open("./Data/"+List1,'r',encoding='iso-8859-1') as inp1,    open("./Data/Aplist_Del_All.csv",'w',encoding='iso-8859-1',newline='')as out:
        rd1 = csv.reader(inp0)
        rd2 = csv.reader(inp1)
        wt = csv.writer(out)
        for row in rd1:
            ap,count = row
            aplist0.append(ap)    # 记录数据集0的aplist
            count0.append(count)
        for row in rd2:              
            ap,count = row
            aplist1.append(ap)    # 记录数据集0的aplist
            count1.append(count)    # 记录数据集1的aplist
        aplist = list(set(aplist0).intersection(aplist1))   # 转到set类型求交集后返回list
        for ap in aplist:
            row = [ap,count0[aplist0.index(ap)],count1[aplist1.index(ap)]]
            wt.writerow(row)     


# In[104]:


#这个函数用于将每行一个ap的数据格式转储为一样一个样本的样式
#输入需要一个AP的列表，用于取得向量各位的排布顺序
#输入需要数据集本身
#输出为一个文件，该文件即是转换后的dataset，前缀Vec_标记
#数据格式：区域号，x，y，样本（[0,0,0,-52,0,-55...]）
def Vectorize(Aplist,Dataset):
    aps = []   # 用于存放读出来的AP列表
    with open("./Data/"+Aplist,'r',encoding='iso-8859-1') as aplist,    open("./Data/"+Dataset,'r',encoding='iso-8859-1') as dataset,    open("./Data/Vec_"+Dataset,'w',encoding='iso-8859-1',newline='') as out:
        rdap = csv.reader(aplist)
        rddat = csv.reader(dataset)
        wt = csv.writer(out)
        for row in rdap:
            aps.append(row[0])    # 读取ap列表
        vect = ['0']*len(aps)     # 创建向量，长度为ap列表
        num = None                  # 记录样本号的变量
        area,x,y = None,None,None  # 记录区域，x，y
        for row in rddat:
            if num == None:
                num = row[0]          # 样本号变为第一个row[0]
            if row[7] not in aps:
                continue
            if row[0] == num:         # 如果该行和上一行同时属于一个样本
                index = aps.index(row[7])
                vect[index] = row[8]    # 填入vector中相应位置的rssi
                area,x,y = row[1],row[2],row[3]  # 更新area，x，y
            else:    #如果进入下一个样本
                wt.writerow([area,x,y]+vect)   # 更新一行样本
                vect = ['0']*len(aps)    # 清空vect
                num = row[0]       # 更新样本号
                index = aps.index(row[7])   # 获取索引
                vect[index] = row[8]     # 填入一个rssi
                area,x,y = row[1],row[2],row[3]  # 更新area，x，y 
                


# In[106]:





# In[ ]:




