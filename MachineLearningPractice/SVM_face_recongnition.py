from __future__ import print_function

from time import time
import logging
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC

print(__doc__)

#display progress logs on stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

###################################################
# download the date, if not already on disk and load it as numpy arrays
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.image.shape

# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print('Total dataset size:')
print ('n_samples: %d' %n_samples)
print('n_features: %d' % n_features)
print ('n_classes: %d' % n_classes)

###################################################
#split into a training set and a test set using a stratified k fold

# split into a training set and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

###################################################
# compute a PCA on the face dataset (treated as unlabled dataset):
# unsupervised feature extraction/dimensionality reduction
n_components = 150

print ('Extracting the top %d eigenfaces from %d faces' % (n_components, X_train.shape[0]))
t0 = time()
pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)
print ('done in %0.3fs' % (time() - t0))

eigenfaces = pca.components_.reshape((n_components, h, w))

print ('Projecting the input data on the eigenfaces arthonormal basis')
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print ('done in %0.3fs' % (time() - t0))

###################################################
# train a SVM classification model

print ('fitting the classifier to the training set')
t0 = time()
param_grid = {'C': [1e3, 5e3, 5e4, 1e5], 'gamma':[0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],}
clf = GridSearchCV(SVC(kernel='rbf', class_weight='auto'),param_grid)
clf = clf.fit(X_train_pca, y_train)
print ('done in %0.3fs' % (time() - t0))
print ('Best estimator found by grid search:')
print (clf.best_estimator_)

###################################################
# Quantitative evaluation of the model quality on the test set

print ("Predicting people's names on the test set")



