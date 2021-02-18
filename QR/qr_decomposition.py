import numpy as np
import math

def norm(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*a[i]
    return math.sqrt(sum)

def QR_decomposition(A):
    a1 = np.array([A[i][0] for i in range(4)])
    a2 = np.array([A[i][1] for i in range(4)])
    a3 = np.array([A[i][2] for i in range(4)])
    a4 = np.array([A[i][3] for i in range(4)])

    b1 = a1

    c1 = a2.dot(b1)/b1.dot(b1)
    b2 = a2 - c1*b1

    c1 = a3.dot(b1)/b1.dot(b1)
    c2 = a3.dot(b2) / b2.dot(b2)
    b3 = a3 - (c1*b1 + c2*b2)

    c1 = a4.dot(b1) / b1.dot(b1)
    c2 = a4.dot(b2) / b2.dot(b2)
    c3 = a4.dot(b3) / b3.dot(b3)
    b4 = a4 - (c1*b1 + c2*b2 + c3*b3)

    Q = np.array([b1/norm(b1), b2/norm(b2), b3/norm(b3), b4/norm(b4)]).transpose()
    R = Q.transpose().dot(A)

    return Q, R