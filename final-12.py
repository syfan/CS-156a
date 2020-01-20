# question 12
from sklearn import svm
import numpy as np

points = np.zeros((7,3))
points[0] = [-1, 1, 0]
points[1] = [-1, 0, 1]
points[2] = [-1, 0, -1]
points[3] = [1, -1, 0]
points[4] = [1, 0, 2]
points[5] = [1, 0, -2]
points[6] = [1, -2, 0]

classifications = points[:, [0]]
data = points[:, [1,2]]

clf = svm.SVC(kernel = 'poly', degree = 2, coef0 = 1.0, gamma = 1)
clf.fit(data, classifications)

print len(clf.support_vectors_)