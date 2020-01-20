# Questions 5-6
from sklearn import svm
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

C = 1
Q = 2

target_digit = 1
vs_digit = 5

test = np.loadtxt("features.test.txt")
train = np.loadtxt("features.train.txt")

digit = []
        
other = []

for row in train:
    if row[0] == target_digit:
        digit.append([row[0], row[1], row[2]])
    elif row[0] == vs_digit:
        other.append([row[0], row[1], row[2]])
digit = np.asarray(digit)
other = np.asarray(other)

trues = np.ones(len(digit))
falses = np.full((len(other), 1), -1)
classifications = np.append(trues, falses)

digit = digit[:, [1, 2]]
other = other[:, [1,2]]
data = np.append(digit, other, axis = 0)

clf = svm.SVC(kernel = 'poly', C=C, degree = Q, coef0 = 1.0, gamma = 1)

clf.fit(data, classifications)

y_pred = clf.predict(data)
comparisons = np.equal(y_pred, classifications)
print 1 - float(np.sum(comparisons)) / len(comparisons)
print len(clf.support_vectors_)