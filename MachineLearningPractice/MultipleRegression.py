from numpy import genfromtxt
import numpy as np
from sklearn import datasets, linear_model

dataPath = r'C:\xxx\xx.csv'
deliveryData = genfromtxt(dataPath, delimiter=',')

print 'data: ', deliveryData

X = deliveryData[:, :-1]
Y = deliveryData[:, -1]

print 'X:', X
print 'Y:', Y

regr = linear_model.linearRegression()

regr.fit(X, Y)

print 'coefficients: ', regr.coef_
print 'intercept: ', regr.intercept_

xPred = [102, 6]
yPred = regr.predict(xPred)
print 'predicted y: ', yPred

