import numpy as np
import random
import matplotlib.pyplot as plt

runs = 1000
d = 2

def prob8_9_10():
    error = 0
    points = 1000
    for q in range(runs):
        xs = np.random.uniform(-1,1, (points, d))
        xs = np.c_[np.ones(points), xs]
        out_sample = np.random.uniform(-1,1, (points, d))
        out_sample = np.c_[np.ones(points), out_sample]
        
        target_points = np.random.uniform(-1,1, (2, d))
        ys = np.zeros(points)
        for i in range(len(xs)):
            det = (xs[i][1] - target_points[0][0]) * (target_points[1][1] - target_points[0][1]) - (xs[i][2] - target_points[0][1]) * (target_points[1][0] - target_points[0][0])
            if det > 0:
                # on one side
                ys[i] = 1
            else:
                # on the other side
                ys[i] = -1        
        
        processed = np.linalg.pinv(xs)
        #weight = np.dot(processed, ys)
        weight = np.array([1, xs[0][0], xs[0][1]])
        weight2 = np.array([1, xs[0][0], xs[0][1], xs[0][0] * xs[0][1], xs[0][0] ** 2, xs[0][1] ** 2])
        # use weight to classify points            
        newys = np.sign(np.dot(np.transpose(weight), np.transpose(xs)))
        outys = np.sign(np.dot(np.transpose(weight), np.transpose(out_sample)))
        noises = np.random.choice(range(points), points / 10, replace = False)
        for noise in noises:
            ys[noise] *= -1
        
        for i in range(len(ys)):
            if (outys[i] != ys[i]):
                error += 1
    print float(error) / (runs * points)
    print weight2