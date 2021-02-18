
def Bisections(polinom, section, eps):
    print("Метод бісекції:")
    iterations = 0
    begin, end = section
    beginValue = polinom.getFuncValue(begin)
    endValue = polinom.getFuncValue(end)

    while (end - begin) >= eps:
        iterations += 1
        middle = (end + begin) / 2
        midValue = polinom.getFuncValue(middle)
        print("Ітерація № {0}. Поточна точка {1} зі значенням {2}".format(iterations, round(middle, 5), round(midValue, 8)))
        print("a = {0}, b = {1}".format(round(begin, 5), round(end, 5)))
        if midValue*beginValue < 0:
            end = middle
            endValue = midValue
        else:
            begin = middle
            beginValue = midValue

    print("Метод бісекції виконаний за {0} ітерацій".format(iterations))
    print()
    return (end + begin) / 2

def Chords(polinom, section, eps):
    print("Метод хорд:")
    iterations = 0
    begin, end = section
    beginValue = polinom.getFuncValue(begin)
    endValue = polinom.getFuncValue(end)

    while True:
        iterations += 1
        crossPoint = (begin * endValue - end * beginValue) / (endValue - beginValue)
        crossPointValue = polinom.getFuncValue(crossPoint)
        print("Ітерація № {0}. Поточна точка {1} зі значенням {2}".format(iterations, round(crossPoint, 5), round(crossPointValue, 8)))
        print("a = {0}, b = {1}".format(round(begin, 5), round(end, 5)))
        if crossPointValue*beginValue < 0:
            end = crossPoint
            endValue = crossPointValue
        else:
            begin = crossPoint
            beginValue = crossPointValue
        if abs(crossPointValue) < eps:
            break

    print("Метод хорд виконаний за {0} ітерацій".format(iterations))
    print()
    return crossPoint

def Newton(polinom, section, eps):
    print("Метод Ньютона:")
    iterations = 0
    begin, end = section
    if polinom.getFuncValue(begin) * polinom.getSecondDerivativeValue(begin) > 0:
        point = begin
    else:
        point = end
    print("Початкові значення. Поточна точка {0} зі значенням {1}".format(round(point, 5), round(polinom.getFuncValue(point), 8)))
    while abs(polinom.getFuncValue(point)) >= eps:
        iterations += 1
        point -= polinom.getFuncValue(point)/polinom.getDerivativeValue(point)
        print("Ітерація № {0}. Поточна точка {1} зі значенням {2}".format(iterations,round(point, 5), round(polinom.getFuncValue(point), 8)))

    print("Метод Ньютона виконаний за {0} ітерацій".format(iterations))
    print()
    return point