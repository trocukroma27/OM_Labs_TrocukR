def absMatrValue(matr):
    for i in range(len(matr)):
        sum = 0
        for j in range(len(matr[i]) if len(matr[i]) else 1):
            sum += matr[i][j]
        if i == 0 or absValue < sum:
            absValue = sum
    return absValue

def multMatr(A, B):
    AB = [0 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
                AB[i] += A[i][j] * B[j]
    return AB

def residualVector(x, x1, n):
    v = [0 for i in range(n)]
    print("Вектор нев'язки:")
    norm_v = 0
    for i in range(n):
        v[i] = abs(x[i] - x1[i])
        print(round(v[i], 6), end="   ")
        if norm_v < v[i]:
            norm_v = v[i]
    print()
    print("Норма нев'язки:")
    print(round(norm_v, 6), end='\n\n')
    return norm_v

def iterationMethod(A, b, n):
    alph = [[0 for j in range(n)] for i in range(n)]
    bet = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                alph[i][j] = 0
            else:
                alph[i][j] = -A[i][j] / A[i][i]
        bet[i] = b[i] / A[i][i]

    print("Матриця A після зведення до виду зручного для ітерацій:")
    for i in range(n):
        for j in range(n):
            print(str(round(alph[i][j], 6)).ljust(11,' '), end = " ")
        print()
    print()

    print("Матриця b після зведення до виду зручного для ітерацій:")
    for i in range(n):
        print(str(round(bet[i], 6)).ljust(11, ' '), end=" ")
    print('\n')

    if absMatrValue(alph) < 1:
        print("Умова збіжності виконана")
    else:
        print("Умова збіжності не виконана")
        quit()

    x = [0 for i in range(n)]
    x1 = [0 for i in range(n)]

    print("Ітерація №0:")
    for i in range(n):
        x[i] = bet[i]
        print("x{0}={1}".format(i+1, round(x[i], 6)), end="   ")
    print('\n')

    f = 1
    while True:
        print("Ітерація №{0}:".format(f))
        for i in range(n):
            x1[i] = x[i]

        sum = multMatr(alph, x1)

        for i in range(n):
            x[i] = bet[i] + sum[i]
            print("x{0}={1}".format(i+1, round(x[i], 6)), end="   ")
        print()

        f += 1

        if residualVector(x, x1, n) < 0.00001:
            break

    print("Розв'язок:")
    for i in range(n):
        print("x{0}={1}".format(i + 1, round(x[i], 6)))



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

print("Матриця A:")
for i in range(n):
    for j in range(n):
        print(str(round(A[i][j], 6)).ljust(11, ' '), end=" ")
    print()
print()

print("Матриця b:")
for i in range(n):
    print(str(round(b[i], 6)).ljust(11, ' '), end=" ")
print('\n')

iterationMethod(A, b, n)
