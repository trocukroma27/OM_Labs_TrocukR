import numpy as np

def function1(x):
    return 1/np.power(27 + np.power(x, 3), 1/3)

def function2(x, y):
    if (y >= np.power(-x, 3) and y <= np.power(x, 1 / 3)) and (x >= 0 and x <= 1):
        return (4 * x * y + 176 * np.power(x, 3) * np.power(y, 3))
    else:
        return 0

def function3(x):
    return (2 * np.power(x, 5/3) + 44 * np.power(x, 13/3) -  2 * np.power(x, 7) - 44 *  np.power(x, 15))

def y1(x):
    return np.power(-x, 3)

def y2(x):
    return np.power(x, 1 / 3)

def rectangle_integrate(func, start, end, n_points = 1000):
    h = (end - start) / n_points
    pts = np.arange(start, end, h)
    result = 0
    for i in range(pts.shape[0] - 1):
        result += func(0.5 * (pts[i] + pts[i+1])) * (pts[i+1] - pts[i])
    return result

def trapeze_integrate(func, start, end, n_points = 1000):
    h = (end - start) / n_points
    pts = np.arange(start, end, h)
    result = 0
    for i in range(pts.shape[0] - 1):
        result += 0.5 * (func(pts[i]) + func(pts[i+1])) * (pts[i+1] - pts[i])
    return result

def parabola_integrate(func, start, end, n_points = 1000):
    h = (end - start) / (2 * n_points)
    pts = np.arange(start, end, h)
    result = 0
    for i in range(1, 2 * n_points - 1, 2):
        result += func(pts[i - 1]) + 4 * func(pts[i]) + func(pts[i + 1])
    return result * h / 3

def double_integrate(func, start, end, n_points=1000):
    values = np.array([])

    h = (end - start) / (2 * n_points)
    x0 = start
    result = 0

    values = np.append(values, func(x0))
    x0 += h

    for i in range(1, 2 * n_points):
        if i % 2 != 0:
            values = np.append(values, 4 * func(x0))
        else:
            values = np.append(values, 2 * func(x0))

        x0 += h

    values= np.append(values, func(x0))
    for i in range(values.size):
        result += values[i]

    return result * h / 3


print("Інтеграл для першої частини")
print("Формула прямокутників: %.3f" %rectangle_integrate(function1, 0, 1.5))
print("Формула трапецій: %.3f" %trapeze_integrate(function1, 0, 1.5))
print("Формула парабол (Сімпсона): %.3f" %parabola_integrate(function1, 0, 1.5))
print()

print("Інтеграл для другої частини")
print("Кубаторна формула: %.3f" %double_integrate(function3, 0, 1, 1000))

