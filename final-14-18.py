# Question 14-18
from sklearn import svm
import numpy as np
from scipy.spatial import distance 

svm_wins = 0
lloyd_wins = 0
points = 100
runs = 100
counter_svm = 0.0
gam = 1.5
k = 9
def same(points1, points2):
    return np.array_equal(points1, points2)

def find_closest_center_index(target_point, center_points):
    best_dist = 10000
    best_center = 0
    center_points = center_points[:, [1,2]]
    for i in range(len(center_points)):
        dist = distance.euclidean(target_point, center_points[i])
        if dist < best_dist:
            best_dist = dist
            best_center = i
    return best_center

def adjust_centers(training_points, center_points):
    for i in range(len(training_points)):
        new_center =find_closest_center_index(training_points[i], center_points)
        training_points[i][0] = new_center
    return training_points

for j in range(runs):
    centers = np.random.uniform(-1,1, (k, 2))
    xs = np.random.uniform(-1,1, (points, 2))
    xs2 = xs
    xs2 = np.c_[np.zeros(len(xs2)), xs2]
    
    classifications = np.zeros(points)
    for i in range(points):
        row = xs[i]
        classifications[i] = int(np.sign(row[1] - row[0] + 
                                         0.25*np.sin(np.pi * row[0])))
    clf = svm.SVC(kernel = 'rbf', gamma = gam)
    
    clf.fit(xs, classifications)
    y_pred = clf.predict(xs)
    comparisons = np.equal(y_pred, classifications)
    ein_svm = 1 - float(np.sum(comparisons)) / len(comparisons)
    if ein_svm == 0:
        counter += 1    
    
    xs2_new = adjust_centers(xs2, centers)
    while (not same(xs2, xs2_new)):
        xs2 = xs2_new
        xs2_new = adjust_centers(xs2_new, centers)
    sum = 0.0
    I = np.zeros((points, k))
    for i in range(points):
        for j in range(k):
            I[i][j] = np.exp(-gam * np.power(np.norm(xs2[k*i + j]) - 
                                             xs2[k*i + j][0]), 2)
    I = np.linalg.pinv(I)
    weight = np.dot(I, comparisons)
    signs_for_lloyd = 0.0
    for i in range(9):
        for j in range(points):
            signs_for_lloyd += np.sign(weight[i] * np.exp(-gam * 
                            np.power(np.norm(xs2[j, [1,2]] - xs2[j][0]), 2)))
        weight[i] = signs_for_lloyd
        signs_for_lloyd = 0
    test_points = np.random.uniform(-1,1, (points, 2))
    test_out_classes = clf.predict(test_points)
    test_out_classes2 = np.sign(np.dot(weight, test_points))

    svm_out = 1 - float(np.sum(test_out_classes)) / len(test_out_classes)
    lloyd_out = 1 - float(np.sum(test_out_classes2)) / len(test_out_classes2)
    if svm_out < lloyd_out:
        svm_wins += 1
    else:
        lloyd_wins += 1
print "SVM won: " + str(svm_wins > lloyd_wins)