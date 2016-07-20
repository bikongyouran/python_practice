from pandas import Series,DataFrame
import pandas as pd

################Series Sample###############################
#
# s = Series([3,'abc',5.4,123456798,''])
# print s

# l = [3,'abc',5.4,123456798,'']
# index = [1,2,3,4,'e']
# s1 = Series(data=l,index=index,name='test')
# s1.index.name = 'index_name'
# print s1
# d = s1[1]
# print "d:" + str(d)
# print s1[2:4]
# print s1[0:2]
# print s1[1:2]

# a = range(10)
# print a


################DataFrame Sample###############################

# d = {'id':[1,2,3,4,5],'name':['a','b','c','d','e'],'value':[9.1,8.2,7.3,6.4,5.5]}
# index = [0,1,2,3,4]
# c = ['name','id','value','other']
# df = DataFrame(data=d,columns=c)
# print df

# d = [(1,2,3,4,5),(9.1,8.2,7.3,6.4,5.5)]
# index = [1,2]
# c = ['name','id','value','other1','other2']
# df = DataFrame(data=d,columns=c,index=index)
# print df

