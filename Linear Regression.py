import numpy as np
import random
import matplotlib.pyplot as plt

runs = 1000
d = 2

def prob5():
    error = 0
    points = 100
    for q in range(runs):
        xs = np.random.uniform(-1,1, (points, d))
        xs = np.c_[np.ones(points), xs]
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
        weight = np.dot(processed, ys)
        # use weight to classify points            
        newys = np.sign(np.dot(np.transpose(weight), np.transpose(xs)))
        
        for i in range(len(ys)):
            if (newys[i] != ys[i]):
                error += 1
    print float(error) / (runs * points)
    
def prob6():
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
        weight = np.dot(processed, ys)
        # use weight to classify points            
        newys = np.sign(np.dot(np.transpose(weight), np.transpose(xs)))
        outys = np.sign(np.dot(np.transpose(weight), np.transpose(out_sample)))
        
        for i in range(len(ys)):
            if (outys[i] != ys[i]):
                error += 1
    print float(error) / (runs * points)
    
    
def prob7():
    error = 0
    points = 10
    total_iterations = 0
    for q in range(runs):
        xs = np.random.uniform(-1,1, (points, d))
        xs = np.c_[np.ones(points), xs]
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
        weight = np.dot(processed, ys)

        errors = points
        while(errors != 0):
            total_iterations += 1
            i = np.random.randint(points)
                        
            out = np.sign(np.dot(np.transpose(weight), np.transpose(xs)))
            if (np.array_equal(out, ys)):
                break
            else:
                weight += xs[i]
            errors -= 1
    print float(total_iterations) / runs
                