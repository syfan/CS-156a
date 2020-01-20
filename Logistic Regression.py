import numpy as np

runs = 100
d = 2

error = 0
points = 100
rate = 0.01
stop_param = 0.01
epochs = 0
for q in range(runs):
    weight = np.zeros(d + 1)
    new_weight = np.zeros(d + 1)    
    xs = np.random.uniform(-1,1, (points, d))
    xs = np.c_[np.ones(points), xs]
    target_points = np.random.uniform(-1,1, (2, d))
    ys = np.zeros(points)
    for i in range(len(xs)):
        det = (xs[i][1] - target_points[0][0]) * (target_points[1][1] - \
            target_points[0][1]) - (xs[i][2] - target_points[0][1]) * \
            (target_points[1][0] - target_points[0][0])
        if det > 0:
            # on one side
            ys[i] = 1
        else:
            # on the other side
            ys[i] = -1        
    while (True):
        epochs += 1
        np.random.shuffle(xs)
        for i in range(points):
            gradient = (ys[i] * xs[i]) / (1 + np.exp(ys[i] * np.inner(weight,xs[i])))
            new_weight = new_weight + (gradient * rate)
        if (np.linalg.norm(weight - new_weight) < stop_param):
            break
        else:
            weight = new_weight
        
    for i in range(len(ys)):
        if (newys[i] != ys[i]):
            error += 1
print float(error) / (runs * points)
print float(epochs) / (runs)
