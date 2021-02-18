import math

def createJakobi(x0, y0, J):
    J[0][0] = y0 / pow(math.cos(x0 * y0 + 0.112), 2) - 2 * x0
    J[0][1] = x0 / pow(math.cos(x0 * y0 + 0.112), 2)
    J[1][0] = 0.482 * x0
    J[1][1] = -3.976 * y0

def inverseJakobi(J, det):
    iJ = [[0 for i in range(2)] for j in range(2)]

    iJ[0][0] = J[1][1] / det
    iJ[0][1] = -J[0][1] / det
    iJ[1][0] = -J[1][0] / det
    iJ[1][1] = J[0][0] / det

    return iJ

def func(x0, y0, arr):
    arr[0] = math.tan(x0 * y0 + 0.112) - x0 * x0
    arr[1] = 0.241 * x0 * x0 - 1.988 * y0 * y0 - 1

def substract(n, a, b, c):
    for i in range(n):
        c[i] = a[i]-b[i]

def multiply(n, A, b, c):
    for i in range(n):
        c[i] = 0
        for j in range(n):
            c[i] += A[i][j] * b[j]

def NewtonMethod(x0, y0, eps):
    f = [1, 1]
    sol = [0 for i in range(2)]
    J = [[0 for i in range(2)] for j in range(2)]
    vector = [1, 1]
    sol[0] = x0
    sol[1] = y0

    k = 0
    while math.fabs(f[0]) > eps or math.fabs(f[1]) > eps:
        k += 1
        createJakobi(x0, y0, J)
        det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        iJ = inverseJakobi(J, det)
        func(x0, y0, f)
        multiply(2, iJ, f, vector)
        substract(2, sol, vector, sol)
        x0 = sol[0]
        y0 = sol[1]


    print("Розв'язок:")
    print(f"x = {round(sol[0], 6)}  y = {round(sol[1], 6)}")
    print(f"f1(x,y) = {round(f[0], 6)}  f2(x,y) = {round(f[1], 6)}")
    print(f"Кількість ітерацій: {k}")
    print()


NewtonMethod(2.5, 0.5, 0.00001)
NewtonMethod(-2.5, -0.5, 0.00001)

