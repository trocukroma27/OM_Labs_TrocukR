import numpy as np

def Scal(A):
    y = np.array([1, 1, 1, 1])
    At = A.transpose()
    A2 = np.linalg.matrix_power(A, 2)
    At2 = np.linalg.matrix_power(At, 2)
    l1 = ((A2.dot(y)).dot((At2.dot(y))))/((A.dot(y)).dot((At2.dot(y))))
    print(f"Ітерація №1: l={l1}")
    p=3
    while True:
        Ap = np.linalg.matrix_power(A, p)
        Atp = np.linalg.matrix_power(At, p)
        Ap1 = np.linalg.matrix_power(A, p-1)

        l2 = ((Ap.dot(y)).dot((Atp.dot(y))))/((Ap1.dot(y)).dot((Atp.dot(y))))
        print(f"Ітерація №{p-1}: l={l1}")

        if abs(l2-l1) < 0.00001:
            break

        p = p + 1
        l1 = l2

    return l2

def Scalmin(A, lmaxa):
    B = np.zeros(shape=(4, 4))
    for i in range(4):
        for j in range(4):
            if i==j:
                B[i][j] = A[i][j] - lmaxa
            else:
                B[i][j] = A[i][j]

    lmaxb = Scal(B)
    return lmaxa + lmaxb


A = np.array([[7.25, 0.9, 1.17, 1.105], [0.9, 3.17, 1.3, 0.16], [1.17, 1.3, 6.43, 2.1], [1.105, 0.16, 2.1, 5.11]])

print("Max:")
lmax = Scal(A)
print(f"lmax={lmax}", end='\n\n')

print("Min:")
lmin = Scalmin(A, lmax)
print(f"lmin={lmin}")