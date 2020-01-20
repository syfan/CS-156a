# Questions 7, 9
import numpy as np

target_digit = 5
lam = 1

test = np.loadtxt("features.test.txt")
train = np.loadtxt("features.train.txt")

digit = []
digit2 = []
other = []
other2 = []
for row in train:
    if row[0] == target_digit:
        digit.append([row[0], row[1], row[2]])
    elif row[0] != target_digit:
        other.append([row[0], row[1], row[2]])
for row in test:
    if row[0] == target_digit:
        digit2.append([row[0], row[1], row[2]])
    elif row[0] != target_digit:
        other2.append([row[0], row[1], row[2]])

other = np.asarray(other)
other2 = np.asarray(other2)
digit = np.c_[np.ones(len(digit)), digit]
other = other[:, [1,2]]
other = np.c_[(np.ones(len(other)) * -1), other]
other2 = other2[:, [1,2]]
other2 = np.c_[(np.ones(len(other2)) * -1), other2]
digit2 = np.c_[np.ones(len(digit2)), digit2]

digit = digit[:, [0, 2, 3]]
new_digits = np.concatenate((digit, other), axis=0)

digit2 = digit2[:, [0,2,3]]
new_digits2 = np.concatenate((digit2, other2), axis=0)

ys = new_digits[:,0]
z = new_digits[:, [1,2]]

z = np.c_[np.ones(len(z)), z]

zt = np.transpose(z)

ztz = np.dot(zt,z)
w_raw = np.linalg.inv(ztz + (lam * np.eye(len(ztz))))
weight = np.dot(w_raw, zt)
weight = np.dot(weight, ys)

newys = np.sign(np.dot(weight, np.transpose(new_digits)))
newys2 = np.sign(np.dot(weight, np.transpose(new_digits2)))
#ein = 1 - np.sum(newys) / len(newys)
ein = float(len(np.where(newys < 0)[0])) / len(newys)
eout = float(len(np.where(newys2 < 0)[0])) / len(newys2)
print "Target digit is " + str(target_digit)
print "E in " + str(ein)
print "E out " + str(eout)
