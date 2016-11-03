from sklearn import datasets
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pickle
from sklearn.externals import joblib

# digits = datasets.load_digits() #the data set is for classification
# iris = datasets.load_iris() #the data set is for classification
# boston = datasets.load_boston() #the data set is for regression
# diabetes = datasets.load_diabetes() #the data set is for regression
# linnerud = datasets.load_linnerud() #the data set is for multivariate regression

# print digits.data
# print digits.data.shape
# print digits.images.shape
# print digits.images[0]
# print digits.target
# print len(digits.data)
# print len(digits.target)
# print digits.target[-10:]

'''
In scikit-learn, an estimator for classification is a Python object
that implements the methods fit(X, y) and predict(T).

When the data is not initially in the (n_samples, n_features) shape, it needs to be preprocessed in order to be used by scikit-learn.

To persist a model, use pickle or joblib for scikit.
joblib is more efficient on big data, but can only pickle to the disk and not to a string.
'''
#####################################################################################
'''svm'''
# digits = datasets.load_digits()
# clf = svm.SVC(gamma=0.001, C=100.)
# clf.fit(digits.data[:-10], digits.target[:-10])
# result = clf.predict(digits.data[-10:])
# print result

# s = pickle.dumps(clf)
# clf2 = pickle.loads(s)
# result2 = clf2.predict(digits.data[-10:])
# print result2

# joblib.dump(clf,"clf.pkl")
# clf3 = joblib.load('clf.pkl')
# result3 = clf3.predict(digits.data[-10:])
# print result3
#####################################################################################
'''knn'''
iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target

indices = np.random.permutation(len(iris_X))#randomly switch the order
iris_X_train = iris_X[indices[:-10]]
iris_Y_train = iris_Y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_Y_test  = iris_Y[indices[-10:]]
#
# iris_X_train = iris_X[:-10]
# iris_Y_train = iris_Y[:-10]
# iris_X_test = iris_X[-10:]
# iris_Y_test = iris_Y[-10:]

knn = KNeighborsClassifier()
knn.fit(iris_X_train,iris_Y_train)
predicted_result = knn.predict(iris_X_test)
print predicted_result
print iris_Y_test
#####################################################################################
