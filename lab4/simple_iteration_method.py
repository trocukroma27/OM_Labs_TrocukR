import math

def simpleIterationMethod(x0, y0, eps):
    print(f"Початкове наближення (x,y)=({x0},{y0})", end='\n\n')

    k = 1

    while True:
        print(f"Ітерація №{k}:")

        x1 = 0.319 - math.cos(y0 - 1.874)
        y1 = (math.sin(x0 + 0.112) - 1.683) / 1.988
        print(f"x = {round(x1, 6)}  y = {round(y1, 6)}")

        dx = math.fabs(x1 - x0)
        dy = math.fabs(y1 - y0)
        print(f"dx = {round(dx, 6)}  dy = {round(dy, 6)}", end='\n\n')

        if dx < eps and dy < eps:
            break

        k += 1
        x0 = x1
        y0 = y1

    print("Розв'язок:")
    print(f"x = {round(x1, 6)}  y = {round(y1, 6)}")
    f1 = math.sin(x1 + 0.112) - 1.988*y1 -1.683
    f2 = x1 + math.cos(y0 - 1.874) - 0.319
    print(f"f1(x,y) = {round(f1, 6)}  f2(x,y) = {round(f2, 6)}")
    print(f"Кількість ітерацій: {k}")


simpleIterationMethod(0.97, -0.4, 0.00001)