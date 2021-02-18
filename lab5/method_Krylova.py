import numpy as np
import math

class Polinom:
    def __init__(self, v):
        self.coefficients = v
        self.derivativeCoefficients = []
        for i in range(1, len(self.coefficients)):
            self.derivativeCoefficients.append(i * self.coefficients[i])
        self.secondDerivativeCoefficients = []
        for i in range(1, len(self.derivativeCoefficients)):
            self.secondDerivativeCoefficients.append(i * self.derivativeCoefficients[i])

    def writePolinom(self):
        polinom = str(round(self.coefficients[0], 4)) + str(round(self.coefficients[1], 4)) + "*\u03bb"
        for i in range(2, len(self.coefficients)):
            if self.coefficients[i] > 0:
                polinom += "+" + str(round(self.coefficients[i], 4)) + "*\u03bb^" + str(i)
            else:
                polinom += str(round(self.coefficients[i], 4)) + "*\u03bb^" + str(i)
        polinom += "=0"
        return polinom

    def getFuncValue(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result +=  math.pow(x, i)*self.coefficients[i]
        return result

    def getDerivativeValue(self, x):
        result = 0
        for i in range(len(self.derivativeCoefficients)):
            result += math.pow(x, i) * self.derivativeCoefficients[i]
        return result

    def getSecondDerivativeValue(self, x):
        result = 0
        for i in range(len(self.secondDerivativeCoefficients)):
            result += math.pow(x, i) * self.secondDerivativeCoefficients[i]
        return result

def Bisections(polinom, section, eps):
    iterations = 0
    begin, end = section
    beginValue = polinom.getFuncValue(begin)
    endValue = polinom.getFuncValue(end)

    while (end - begin) >= eps:
        iterations += 1
        middle = (end + begin) / 2
        midValue = polinom.getFuncValue(middle)
        if midValue*beginValue < 0:
            end = middle
            endValue = midValue
        else:
            begin = middle
            beginValue = midValue

    return (end + begin) / 2

def decompLU(A):
    n = len(A)

    L = np.zeros(shape = (n, n))
    U = np.zeros(shape = (n, n))

    for i in range(0, n):
        L[i][i] = 1
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - sum

        for j in range(i + 1, n):
            sum = 0
            for k in range(i):
                sum += L[j][k] * U[k][i]
            L[j][i] = (1 / U[i][i]) * (A[j][i] - sum)


    return L, U

def slau_solution(n, b, L, U):
    y = np.zeros(shape=4)
    x = np.zeros(shape=4)
    y[0] = b[0]

    for i in range(1, n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]
        y[i] = b[i] - sum

    if U[n-1][n-1] == 0 and y[0] == 0:
        print("Дана система має безліч розв'язків")
        return
    if U[n-1][n-1] == 0 and y[0] != 0:
        print("Дана система не має розв'язків")
        return

    x[n-1] = y[n-1] / U[n-1][n-1]
    for i in range(2, n + 1):
        sum = 0
        for j in range(1, i):
            sum += U[n-i][n-j] * x[n-j]
        x[n-i] = (y[n-i] - sum) / U[n-i][n-i]

    return x

def methodKrilova(A):
    print("Вхідна матриця:")
    print(A, end='\n\n')
    Y=np.zeros(shape=(4,4))
    y = [1, 0, 0, 0]
    for i in range(4):
        print(f"y{i}:")
        for j in range(4):
            print(y[j])
        print()
        Y[3-i] = y
        y = A.dot(y)

    Y = Y.transpose()

    L, U = decompLU(Y)
    p = slau_solution(4, -y, L, U)
    p1 = p[::-1]
    p1 = np.append(p1, [1])

    polinom = Polinom(p1)
    print(f"det(A-\u03bbE)={polinom.writePolinom()}")
    print()

    x1 = Bisections(polinom, [2, 3], 0.001)
    x2 = Bisections(polinom, [3, 4], 0.001)
    x3 = Bisections(polinom, [5.8, 6.2], 0.001)
    x4 = Bisections(polinom, [8.5, 10], 0.001)

    print("Власні значення:")
    print(f"\u03bb{1}={round(x1, 2)}")
    print(f"\u03bb{2}={round(x2, 2)}")
    print(f"\u03bb{3}={round(x3, 2)}")
    print(f"\u03bb{4}={round(x4, 2)}")
    print()

    print("Власні вектори:", end="\n\n")
    print(f"Власний вектор для \u03bb{1}={round(x1, 2)}:")
    q0 = 1
    q1 = x1*q0+p[0]
    q2 = x1*q1+p[1]
    q3 = x1*q2+p[2]

    v1 = Y.transpose()[0] + q1 * Y.transpose()[1] + q2 * Y.transpose()[2] + q3 * Y.transpose()[3]
    v1 = v1 / v1[3]
    for i in range(4):
        print(round(v1[i], 4))
    print()
    u = A.dot(v1) - x1 * v1
    print("Вектор нев'язки:")
    for i in range(4):
        print(round(u[i], 1))
    print()

    print(f"Власний вектор для \u03bb{2}={round(x2, 2)}:")
    q0 = 1
    q1 = x2 * q0 + p[0]
    q2 = x2 * q1 + p[1]
    q3 = x2 * q2 + p[2]

    v2 = Y.transpose()[0] + q1 * Y.transpose()[1] + q2 * Y.transpose()[2] + q3 * Y.transpose()[3]
    v2 = v2 / v2[3]
    for i in range(4):
        print(round(v2[i], 4))
    print()
    u = A.dot(v2) - x2 * v2
    print("Вектор нев'язки:")
    for i in range(4):
        print(round(u[i], 1))
    print()

    print(f"Власний вектор для \u03bb{3}={round(x3, 2)}:")
    q0 = 1
    q1 = x3 * q0 + p[0]
    q2 = x3 * q1 + p[1]
    q3 = x3 * q2 + p[2]

    v3 = Y.transpose()[0] + q1 * Y.transpose()[1] + q2 * Y.transpose()[2] + q3 * Y.transpose()[3]
    v3 = v3 / v3[3]
    for i in range(4):
        print(round(v3[i], 4))
    print()
    u = A.dot(v3) - x3 * v3
    print("Вектор нев'язки:")
    for i in range(4):
        print(round(u[i], 1))
    print()

    print(f"Власний вектор для \u03bb{4}={round(x4, 2)}:")
    q0 = 1
    q1 = x4 * q0 + p[0]
    q2 = x4 * q1 + p[1]
    q3 = x4 * q2 + p[2]

    v4 = Y.transpose()[0] + q1 * Y.transpose()[1] + q2 * Y.transpose()[2] + q3 * Y.transpose()[3]
    v4 = v4 / v4[3]
    for i in range(4):
        print(round(v4[i], 4))
    print()
    u = A.dot(v4) - x4 * v4
    print("Вектор нев'язки:")
    for i in range(4):
        print(round(u[i], 1))
    print()



A = np.array([[7.25, 0.9, 1.17, 1.105], [0.9, 3.17, 1.3, 0.16], [1.17, 1.3, 6.43, 2.1], [1.105, 0.16, 2.1, 5.11]])

methodKrilova(A)