from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

#Read in the csv file and put features in a list of dict and list of class label
allElectronicsData = open(r'C:\codes\python_practice\MachineLearningPractice\decisionTreeSample.csv', 'rb')
reader = csv.reader(allElectronicsData)
headers = reader.next()

print headers

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)

print featureList

#Vectorize features, transform original to 0 1 format.
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print 'dummyX:' + str(dummyX)
print vec.get_feature_names()

print 'labelList:' + str(labelList)

#Vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print 'dummyY:' + str(dummyY)

#use decision tree for classification
#clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)
print 'clf:' + str(clf)

#Visulize model, should install Graphviz to your computer.
# with open('xxx.dot', 'w') as f:
#     f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(),out_file=f)
dot_data = StringIO()
tree.export_graphviz(clf, feature_names=vec.get_feature_names(),out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('dt.pdf')

oneRowX = dummyX[0, :]
print 'oneRowX:' + str(oneRowX)

#construct a test sample,just use the first row and change one feature value.
newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print 'newRowX:' + str(newRowX)

predictedY = clf.predict(newRowX)
print 'predictedY:' + str(predictedY)
