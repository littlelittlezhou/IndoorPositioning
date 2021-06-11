文件说明：
1.原始数据集。0表示由设备0采集。
dataset_0.csv
dataset_1.csv
2.删除数据集。删除最后一列找不到rssi的条目。
Del_dataset_0.csv
Del_dataset_1.csv
3.数据集中AP列表。0，1，all分别代表是数据集0，数据集1和两个合起来的ap列表。
Aplist_Del_All.csv
ApList_Del_dataset_0.csv
ApList_Del_dataset_1.csv
4.向量化数据。形式为：区域，x，y，样本
Vec_Del_dataset_0.csv
Vec_Del_dataset_1.csv
5.虚拟AP位置，每个区域占3行，第一行是AP号，后两行对应位置是x，y坐标
VAP_eta_1.csv
VAP_eta_0.csv
6.pkl，存档的变量
rss_1m_*.pkl  : 保存的虚拟AP在1m处的rssi，其中，*为数字，代表数据集标记。这个变量受到vap位置和eta的影响。该变量的形式为：字典，键为区域，整型；值为rssi值，列表，长度为469.
vaploc_*.pkl  :保存的虚拟ap的位置，该文件和5具有同样的信息量但是文件名中未标记eta。*同样表示数据集。
该变量的形式为：字典，键为区域，值为由三个列表组成的元组，（ap编号，x坐标，y坐标）按索引对应。
7.已经划分且打乱但是并未处理的数据集，数据格式与4相同。
Train_*.csv
Test_*.csv
8. 测试eta时使用的中间变量。存放于./EtaTest/
rss_1m_*_?.pkl，含义同6，？处为生成该文件时设定的eta值。  
VAP_?_*.csv，含义同5，？处为eta。
vaploc_*_?.pkl,同6。
9.存放每个eta时定位准确度的文件。
eta.txt
10. ordered，当aplist按出现次数排序后，按此影响每个样本的每维对应ap后生成的数据。