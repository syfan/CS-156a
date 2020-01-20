# Question 8
# this version of the code uses a feature transform
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
digit2 = np.c_[np.ones(len(digit2)), digit2]
other = other[:, [1,2]]
new_other = np.zeros([len(other), 6])
for i in range(len(other)):
    row = other[i]
    new_other[i] = [1, row[0], row[1], row[0]*row[1], row[0] ** 2, row[1] ** 2]
other = new_other
other = np.c_[(np.ones(len(other)) * -1), other]

new_other2 = np.zeros([len(other2), 6])
for i in range(len(other2)):
    row = other2[i]
    new_other2[i] = [1, row[0], row[1], row[0]*row[1], row[0] ** 2, row[1] ** 2]
other2 = new_other2
other2 = np.c_[(np.ones(len(other2)) * -1), other2]

digit = digit[:, [0, 2, 3]]
new_digit = np.zeros([len(digit), 6])
for i in range(len(digit)):
    row = digit[i]
    new_digit[i] = [1, row[1], row[2], row[1]*row[2], row[1] ** 2, row[2] ** 2]
digit = new_digit
digit = np.c_[np.ones(len(digit)), digit]

digit2 = digit2[:, [0, 2, 3]]
new_digit2 = np.zeros([len(digit2), 6])
for i in range(len(digit2)):
    row = digit2[i]
    new_digit2[i] = [1, row[1], row[2], row[1]*row[2], row[1] ** 2, row[2] ** 2]
digit2 = new_digit2
digit2 = np.c_[np.ones(len(digit2)), digit2]

new_digits = np.concatenate((digit, other), axis=0)
new_digits2 = np.concatenate((digit2, other2), axis=0)

ys = new_digits[:,0]
ys2 = new_digits2[:0]
z = new_digits[:, [1,2,3,4,5,6]]
z2 = new_digits2[:, [1,2,3,4,5,6]]

zt = np.transpose(z)

ztz = np.dot(zt,z)
w_raw = np.linalg.inv(ztz + (lam * np.eye(len(ztz))))
weight = np.dot(w_raw, zt)
weight = np.dot(weight, ys)

newys = np.sign(np.dot(weight, np.transpose(z)))
newys2 = np.sign(np.dot(weight, np.transpose(z2)))
ein = float(len(np.where(newys == 1)[0])) / len(newys)
eout = float(len(np.where(newys2 == 1)[0])) / len(newys2)
print "Target digit is " + str(target_digit)
print "E in " + str(ein)
print "E out " + str(eout)
