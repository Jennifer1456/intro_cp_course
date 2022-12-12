def minus(a, b):
    result = []
    for i in range(min(len(a), len(b))):
        result.append(a[i] - b[i])

    if len(a) > len(b):
        result.extend(a[len(b) 🙂)
    else:
        result.extend(b[len(a) 🙂)
    return result


def multiply_const(p, a):
    result = []
    for i in range(len(p)):
        result.append(p[i] * a)
    return result


def divide_const(p, a):
    result = []
    for i in range(len(p)):
        result.append(p[i] / a)
    return result


def multiply_x(a):
    a.insert(0, 0)
    return a


def calc_poly(a, x):
    result = 0
    for i in range(len(a)):
        result += a[i] * x ** i
    return result


def legendre(n):
    if n == 0:
        P_n = [1]
    elif n == 1:
        P_n = [0, 1]
    else:
        P_n = divide_const(
            minus(
                multiply_const(multiply_x(legendre(n - 1)), 2 * n - 1),
                multiply_const(legendre(n - 2), n - 1),
            ),
            n,
        )
    return P_n

# n = int(input())
# x = int(input())
# P = legendre(n)
# print(calc_poly(P, x))

class Poly:

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __add__(self, other):
        result = []
        for i in range(min(len(self.coeffs), len(other.coeffs))):
            result.append(self.coeffs[i] + other.coeffs[i])

        if len(self.coeffs) > len(other.coeffs):
            result.extend(self.coeffs[len(other.coeffs) 🙂)
        else:
            result.extend(other.coeffs[len(self.coeffs) 🙂)
        return result

a = Poly([1, 2, 3])
b = Poly([4, 5, 6])
print(a + b)  # a.__add__(b)
