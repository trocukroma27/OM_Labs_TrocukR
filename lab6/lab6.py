import math
import matplotlib.pyplot as plt

def func(x):
    return (4-x)*math.exp(x-3)

def NewtonForward(x, n, arr_x, arr_y):
    res = arr_y[0]
    for i in range(1, n):
        F = 0
        for j in range(i + 1):
            den = 1
            for k in range(i + 1):
                if k != j:
                    den *= (arr_x[j] - arr_x[k])
            F += arr_y[j] / den
        for k in range(i):
            F *= (x - arr_x[k])
        res += F

    return res

def NewtonBack(x, n, arr_x, arr_y):
    res = arr_y[n-1]
    for i in reversed(range(n-1)):
        F = 0
        for j in reversed(range(i, n)):
            den = 1
            for k in reversed(range(i, n)):
                if k != j:
                    den *= (arr_x[j] - arr_x[k])
            F += arr_y[j] / den
        for k in reversed(range(i+1, n)):
            F *= (x - arr_x[k])
        res += F

    return res

def Lagrange(x, arr_x, arr_y, n):
    lagrange_pol = 0
    for i in range(n):
        basic_pol = 1
        for j in range(n):
            if i == j:
                continue
            basic_pol *= (x - arr_x[j]) / (arr_x[i] - arr_x[j])
        lagrange_pol += basic_pol * arr_y[i]

    return  lagrange_pol


class SplineTuple:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x

def BuildSpline(x, y, n):
    splines = [SplineTuple(0, 0, 0, 0, 0) for _ in range(n)]
    for i in range(n):
        splines[i].x = x[i]
        splines[i].a = y[i]

    splines[0].c = splines[n - 1].c = 0.0

    alpha = [0.0 for _ in range(n - 1)]
    beta = [0.0 for _ in range(n - 1)]

    for i in range(1, n - 1):
        hi = x[i] - x[i - 1]
        hi1 = x[i + 1] - x[i]
        A = hi
        C = 2.0 * (hi + hi1)
        B = hi1
        F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
        z = (A * alpha[i - 1] + C)
        alpha[i] = -B / z
        beta[i] = (F - A * beta[i - 1]) / z

    for i in range(n - 2, 0, -1):
        splines[i].c = alpha[i] * splines[i + 1].c + beta[i]

    for i in range(n - 1, 0, -1):
        hi = x[i] - x[i - 1]
        splines[i].d = (splines[i].c - splines[i - 1].c) / hi
        splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (y[i] - y[i - 1]) / hi
    return splines

def Interpolate(splines, x):
    if not splines:
        return None

    n = len(splines)
    s = SplineTuple(0, 0, 0, 0, 0)

    if x <= splines[0].x:
        s = splines[0]
    elif x >= splines[n - 1].x:
        s = splines[n - 1]
    else:
        i = 0
        j = n - 1
        while i + 1 < j:
            k = i + (j - i) // 2
            if x <= splines[k].x:
                j = k
            else:
                i = k
        s = splines[j]

    dx = x - s.x

    return s.a + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx;



n = int(input("Введіть кількість вузлів інтерполяції: "))

arr_x = [0 for i in range(n)]
arr_y = [0 for i in range(n)]

for i in range(n):
    arr_x[i] = float(input(f"x{i+1} = "))
    arr_y[i] = func(arr_x[i])

x = float(input("Введіть х, в якому треба знайти значення функції: "))

f = round(func(x), 6)
print(f"f(x) = {f}")

lagr = round(Lagrange(x, arr_x, arr_y, n), 6)
print(f"Інтерполяція Лагранжа в точці {x} рівна F = {lagr}")
print(f"Помилка інтерполяції: {round(abs(f - lagr), 6)}")

newt_f = round(NewtonForward(x, n, arr_x, arr_y), 6)
print(f"Інтерполяція Ньютона вперед в точці {x} рівна F = {newt_f}")
print(f"Помилка інтерполяції: {round(abs(f - newt_f), 6)}")

newt_b = round(NewtonBack(x, n, arr_x, arr_y), 6)
print(f"Інтерполяція Ньютона назад в точці {x} рівна F = {newt_b}")
print(f"Помилка інтерполяції: {round(abs(f - newt_b), 6)}")

spline = BuildSpline(arr_x, arr_y, n)
s = round(Interpolate(spline, x), 6)
print(f"Сплаймами в точці {x} рівна F = {s}")
print(f"Помилка інтерполяції: {round(abs(f - s), 6)}")


xi = arr_x[0]
dx = (arr_x[1] - arr_x[0]) / 5
X = []
F = []
INTER = []
DELTA_LAGR = []

while xi <= arr_x[n - 1]:
    X.append(xi)
    f = func(xi)
    F. append(f)
    lagr = Lagrange(xi, arr_x, arr_y, n)
    INTER.append(lagr)
    DELTA_LAGR.append(abs(f - lagr))
    xi += dx
plt.plot(X, F, label = "Функція", linestyle='--')
plt.plot(X, INTER, label = "Інтерполяція Лагранжа", linestyle='-.')
plt.plot(X, DELTA_LAGR, label = "Помилка")
plt.legend()
plt.title("Лагранж")
plt.show()



xi = arr_x[0]
INTER = []
DELTA_NF = []
i=0
while xi <= arr_x[n - 1]:
    newt_f = NewtonForward(xi, n, arr_x, arr_y)
    INTER.append(newt_f)
    DELTA_NF.append(abs(F[i] - newt_f))
    xi += dx
    i += 1
plt.plot(X, F, label = "Функція", linestyle='--')
plt.plot(X, INTER, label = "Інтерполяція Ньютона вперед", linestyle='-.')
plt.plot(X, DELTA_NF, label = "Помилка")
plt.legend()
plt.title("Ньютон вперед")
plt.show()


xi = arr_x[0]
INTER = []
DELTA_NB = []
i=0
while xi <= arr_x[n - 1]:
    newt_b = NewtonBack(xi, n, arr_x, arr_y)
    INTER.append(newt_b)
    DELTA_NB.append(abs(F[i] - newt_b))
    xi += dx
    i += 1
plt.plot(X, F, label = "Функція", linestyle='--')
plt.plot(X, INTER, label = "Інтерполяція Ньютона назад", linestyle='-.')
plt.plot(X, DELTA_NB, label = "Помилка")
plt.legend()
plt.title("Ньютон назад")
plt.show()


xi = arr_x[0]
INTER = []
DELTA_SPL = []
i=0
spline = BuildSpline(arr_x, arr_y, n)
while xi <= arr_x[n - 1]:
    s = Interpolate(spline, xi)
    INTER.append(s)
    DELTA_SPL.append(abs(F[i] - s))
    xi += dx
    i += 1
plt.plot(X, F, label = "Функція", linestyle='--')
plt.plot(X, INTER, label = "Сплайн", linestyle='-.')
plt.plot(X, DELTA_SPL, label = "Помилка")
plt.legend()
plt.title("Сплайн третього порядку")
plt.show()

plt.plot(X, DELTA_LAGR, label = "Помилка інтерполації Лагранжа", linestyle='--')
plt.plot(X, DELTA_NF, label = "Помилка інтерполації Ньютона вперед", linestyle='-.')
plt.plot(X, DELTA_NB, label = "Помилка інтерполації Ньтона назад", linestyle=':')
plt.plot(X, DELTA_SPL, label = "Помилка сплайну")
plt.legend()
plt.show()