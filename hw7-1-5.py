# questions 1-5
import numpy as np
import matplotlib.pyplot as plt

in_file = np.loadtxt("in.dta.txt")
out_file =np.loadtxt("out.dta.txt")

training = in_file[:25]
validation = in_file[25:]

transformed_in = np.empty([len(training), 8])
transformed_out = np.empty([len(out_file), 8])

for i in range(len(training)):
    x1 = training[i][0]
    x2 = training[i][1]
    transformed_in[i] = (1, x1, x2, np.power(x1, 2), np.power(x2, 2), x1 * x2, np.abs(x1 - x2), np.abs(x1 + x2))
    
    
for i in range(len(out_file)):
    x1 = out_file[i][0]
    x2 = out_file[i][1]
    transformed_out[i] = (1, x1, x2, np.power(x1, 2), np.power(x2, 2), x1 * x2, np.abs(x1 - x2), np.abs(x1 + x2))

in_error = 0
out_error = 0 
processed = np.linalg.pinv(transformed_in)

weight = np.dot(processed, training)
newys = np.sign(np.dot(weight, np.transpose(training)))
check_out = np.sign(np.dot(weight, np.transpose(out_file)))

for i in range(len(newys)):
    if (newys[i][0] != training[i][2]):
        in_error += 1
for i in range(len(check_out)):
    if (check_out[i][0] != out_file[i][2]):
        out_error += 1
k = 6
in_error += (np.power(10, k) / len(training)) * (np.sum(np.power(in_error, 2)))
print float(in_error) / len(training)
print float(out_error) / len(out_file)