import math

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





n = int(input("Введіть кількість вузлів інтерполяції: "))

arr_x = [0 for i in range(n)]
arr_y = [0 for i in range(n)]

for i in range(n):
    arr_x[i] = float(input(f"x{i+1} = "))
    arr_y[i] = func(arr_x[i])

x = float(input("Введіть х, в якому треба знайти значення функції: "))
f = round(func(x), 6)
lagr = round(Lagrange(x, arr_x, arr_y, n), 6)
newt_f = round(NewtonForward(x, n, arr_x, arr_y), 6)
newt_b = round(NewtonBack(x, n, arr_x, arr_y), 6)
print(f"f(x) = {f}")
print(f"Інтерполяція Лагранжа в точці {x} рівна F = {lagr}")
print(f"Помилка інтерполяції: {abs(f - lagr)}")
print(f"Інтерполяція Ньютона вперед в точці {x} рівна F = {newt_f}")
print(f"Помилка інтерполяції: {abs(f - newt_f)}")
print(f"Інтерполяція Ньютона назад в точці {x} рівна F = {newt_b}")
print(f"Помилка інтерполяції: {abs(f - newt_b)}")


