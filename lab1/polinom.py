import math
import methods

class Polinom:
    def __init__(self, v):
        self.coefficients = v
        self.derivativeCoefficients = []
        for i in range(1, len(self.coefficients)):
            self.derivativeCoefficients.append(i * self.coefficients[i])
        self.secondDerivativeCoefficients = []
        for i in range(1, len(self.derivativeCoefficients)):
            self.secondDerivativeCoefficients.append(i * self.derivativeCoefficients[i])

    def writePolinom(self):
        polinom = str(self.coefficients[0]) + str(self.coefficients[1])
        for i in range(2, len(self.coefficients)):
            if self.coefficients[i] > 0:
                polinom += "+" + str(self.coefficients[i]) + "*x^" + str(i)
            else:
                polinom += str(self.coefficients[i]) + "*x^" + str(i)
        polinom += "=0"
        return polinom

    def getFuncValue(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result +=  math.pow(x, i)*self.coefficients[i]
        return result

    def getDerivativeValue(self, x):
        result = 0
        for i in range(len(self.derivativeCoefficients)):
            result += math.pow(x, i) * self.derivativeCoefficients[i]
        return result

    def getSecondDerivativeValue(self, x):
        result = 0
        for i in range(len(self.secondDerivativeCoefficients)):
            result += math.pow(x, i) * self.secondDerivativeCoefficients[i]
        return result

    def SolveAll(self, sections, eps):
        solutions = []
        i = 1
        for section in sections:
            print("Корінь №", i)
            print("Інтервал №", section)
            solutions.append(self.Solve(section, eps))
            i += 1
        return solutions

    def Solve(self, section, eps):
        result1 = methods.Bisections(self, section, eps)
        result2 = methods.Chords(self, section, eps)
        result3 = methods.Newton(self, section, eps)
        result = [result1, result2, result3]
        return result