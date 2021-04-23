import numpy as np
import matplotlib.pyplot as plt

def analyt(x):
    return x**2

def func(x, y):
    return 3 * x - y / x

x0 = 1
y0 = 1
h = 0.01

def runge(func, x0, x1, y0, h):
    yk = y0
    x = np.arange(x0+h, x1, h)
    res = []
    res.append(y0)

    for i in range(x.shape[0]):
        k1 = func(x[i], yk)
        k2 = func(x[i] + h / 2, yk + h * k1 / 2)
        k3 = func(x[i] + h / 2, yk + h * k2 / 2)
        k4 = func(x[i] + h, yk + h * k3)

        yk += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        res.append(yk)

    return res

def adams(func, x0, x1, y0, h):
    res = runge(func, x0, x0 + h * 3, y0, h)

    const = np.asarray([1 / 24, -5 / 24, 19 / 24, 3 / 8], dtype=np.float32)
    x = np.asarray([x0, x0 + h, x0 + 2 * h, x0 + 3 * h], dtype=np.float32)

    for _ in range(len(np.arange(x0 + h * 3, x1 - h , h))):
        f = np.asarray(func(x[-4:], res[-4:]))
        yk = res[-1] + h * np.sum(f * const)
        res.append(yk)
        x = np.append(x, [x[-1] + h])
    return res

x = x0
X = []
analyt_res = []
for i in range(len(np.arange(x0, x0 + 1, h))):
    X.append(x)
    analyt_res.append(analyt(x))
    x += 0.01

runge_res = runge(func, x0, x0 + 1, y0, h)
delta_r = [abs(analyt_res[i] - runge_res[i]) for i in range(len(analyt_res))]

adams_res = adams(func, x0, x0 + 1, y0, h)
delta_a = [abs(analyt_res[i] - adams_res[i]) for i in range(len(analyt_res))]

max_delta = [max(delta_r[i], delta_a[i]) for i in range(len(delta_r))]

print(f"Початкове значення x = {x0}")
print(f"Крок h = {h}", end="\n\n")

print("Метод Рунге-Кутта")
print(f"{'Аналітичне значення':<22} {'Значення методу':<22} {'Помилка':<22}")
for i in range(len(analyt_res)):
    print(f"{analyt_res[i]:<22} {runge_res[i]:<22} {delta_r[i]:<22}")
print()

print("Метод Адамса")
print(f"{'Аналітичне значення':<22} {'Значення методу':<22} {'Помилка':<22}")
for i in range(len(analyt_res)):
    print(f"{analyt_res[i]:<22} {adams_res[i]:<22} {delta_a[i]:<22}")

plt.plot(X, analyt_res, label = "Аналітичне значення", linestyle='--')
plt.plot(X, runge_res, label = "Значення методу", linestyle='-.')
plt.plot(X, delta_r, label = "Помилка")
plt.legend()
plt.title("Метод Рунге-Кутта")
plt.show()

plt.plot(X, analyt_res, label = "Аналітичне значення", linestyle='--')
plt.plot(X, adams_res, label = "Значення методу", linestyle='-.')
plt.plot(X, delta_a, label = "Помилка")
plt.legend()
plt.title("Метод Адамса")
plt.show()

plt.plot(X, max_delta)
plt.title("Максимальна помилка")
plt.show()