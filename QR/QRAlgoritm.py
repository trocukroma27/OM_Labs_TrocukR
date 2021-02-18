import numpy as np

def qr_householder(A):

    Q = np.identity(4)

    R = np.copy(A)

    for n in range(4):
        x = A[n:, n]
        k = x.shape[0]

        ro = -np.sign(x[0]) * np.linalg.norm(x)

        e = np.zeros(k)
        e[0] = 1
        v = (1 / (x[0] - ro)) * (x - (ro * e))

        for i in range(4):
            R[n:, i] = R[n:, i] - (2 / (v@v)) * ((np.outer(v, v)) @ R[n:, i])

        for i in range(4):
            Q[n:, i] = Q[n:, i] - (2 / (v@v)) * ((np.outer(v, v)) @ Q[n:, i])

    return Q.transpose(), R

def QR(A):
    check = True
    while check:
        check = False
        Q, R = qr_householder(A)
        A = R.dot(Q)
        for i in range(1, 4):
            for j in range(i):
                if A[i][j] > 0.001:
                    check = True
    print("Власні значення:")
    for i in range(4):
        print(f"\u03bb{i+1}={round(A[i][i], 2)}")


A = np.array([[7.25, 0.9, 1.17, 1.105], [0.9, 3.17, 1.3, 0.16], [1.17, 1.3, 6.43, 2.1], [1.105, 0.16, 2.1, 5.11]])
QR(A)