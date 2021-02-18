def printSys(A, b):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print(str(A[i][j]).ljust(6, ' '), end="   ")
        print("| ", b[i])
    print()

def printMatr(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(str(round(A[i][j], 6)).ljust(11,' '), end = " ")
        print()
    print()

def printMatr2(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print("{0:e}".format(A[i][j]), end = "   ")
        print()
    print()

def multMatr(A, B):
    n = len(A)
    AB = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                AB[i][j] += A[i][k] * B[k][j]
    return AB


def printVector(v):
    for i in range(len(v)):
        print(round(v[i], 6))
    print()

def decompLU(A):
    n = len(A)

    L = [[0 for j in range(n)] for i in range(n)]
    U = [[0 for j in range(n)] for i in range(n)]

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
    y = [0 for i in range(n)]
    x = [0 for i in range(n)]
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

    return x, y

def determ(U):
    d = 1
    for i in range(len(U)):
        d *= U[i][i]

    return d

def chage_matr(arr, i):
    for j in range(i):
        arr[j] = 0
    arr[i] = 1

def inverseA(L, U, A):
    n = len(A)
    arr = [0 for i in range(n)]
    d = determ(U)

    if d == 0:
        print("Оберненої матриці не існує")
        return

    for i in range(n):
        chage_matr(arr, i)
        sol = slau_solution(n, arr, L, U)[0]
        for j in range(n):
            A[j][i] = sol[j]

def residualVector(A, x, b):
    n = len(A)
    v = [0 for i in range(n)]
    res = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            res[i] += A[i][j] * x[j]

    for i in range(n):
        v[i] = b[i] - res[i]

    return v


n = int(input("Ввеведіть розмірність:"))

f = open("input.txt", "r")
data = f.read()
A = [[0 for j in range(n)] for i in range(n)]
b = [0 for j in range(n)]
for i in range(n):
    for j in range(n + 1):
        if j != n:
            A[i][j] = float(data.split()[i*6+j])
        else:
            b[i] = float(data.split()[i * 6 + j])

x = [0 for i in range(n)]
y = [0 for i in range(n)]

print("Система рівнянь:")
printSys(A, b)

L, U = decompLU(A)
print("Матриця L:")
printMatr(L)
print("Матриця U:")
printMatr(U)

x, y = slau_solution(n, b, L, U)
print("Перший крок - розв'язок системи Ly = b.")
print("Вектор y:")
printVector(y)
print("Другий крок - знаходження рішення нашої початкової системи шляхом розв'язку системи Ux = y.")
print("Вектор x:")
printVector(x)

d = determ(U)
print("det(A) = ", round(d, 6), end="\n\n")

iA = [[0 for j in range(n)] for i in range(n)]
inverseA(L, U, iA)
print("A^-1:")
printMatr(iA)

AiA = multMatr(A, iA)
print("A*A^-1:")
printMatr2(AiA)

v = residualVector(A, x, b)
print("Вектор невязки:")
for i in range(n):
    print("{0:e}".format(v[i]))
