# Question 13
from sklearn import svm
import numpy as np

points = 100
runs = 100
counter = 0.0
gam = 1.5

for j in range(runs):
    xs = np.random.uniform(-1,1, (points, 2))
    classifications = np.zeros(points)
    for i in range(points):
        row = xs[i]
        classifications[i] = int(np.sign(row[1] - row[0] + 
                                         0.25*np.sin(np.pi * row[0])))
    clf = svm.SVC(kernel = 'rbf', gamma = gam)
    
    clf.fit(xs, classifications)    
    y_pred = clf.predict(xs)
    comparisons = np.equal(y_pred, classifications)
    ein = 1 - float(np.sum(comparisons)) / len(comparisons)
    if ein == 0:
        counter += 1
print counter / runs