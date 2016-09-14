# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy

final = open('c:/test/final.dat' , 'r')

data = [line.strip().split('\t') for line in final]
feature = [[float(x) for x in row[3:]] for row in data]

#调用kmeans类
clf = KMeans(n_clusters=9)
s = clf.fit(feature)
print s

#9个中心
print clf.cluster_centers_

#每个样本所属的簇
print clf.labels_

#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
print clf.inertia_

#进行预测
print clf.predict(feature)

#保存模型
joblib.dump(clf , 'c:/km.pkl')

#载入保存的模型
clf = joblib.load('c:/km.pkl')

'''
#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
for i in range(5,30,1):
    clf = KMeans(n_clusters=i)
    s = clf.fit(feature)
    print i , clf.inertia_
'''