import polinom

v = [-7, -3, -9, -2, 1]
sections = [[-3, -2], [4, 5]]
print(polinom.Polinom(v).writePolinom())
print()
solutions = polinom.Polinom(v).SolveAll(sections, 0.00001)
i = 1
for solution in solutions:
    print("Корінь №", i)
    print("Метод бісекції:", round(solution[0], 5))
    print("Метод хорд:", round(solution[1], 5))
    print("Метод Ньютона:", round(solution[2], 5))
    print()
    i += 1

