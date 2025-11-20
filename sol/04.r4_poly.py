from fractions import Fraction


def differentiate(poly: Polynomial) -> Polynomial:
    res = poly.copy()
    res.pop()

    if res == []:
        return [Fraction(0)]

    for i in range(len(res)):
        res[i] *= len(res) - i

    return res


def integrate(poly: Polynomial) -> Polynomial:
    res = poly.copy()

    if res == [Fraction(0)]:
        return res

    for i in range(len(res)):
        res[i] = Fraction(res[i], len(res) - i)

    res.append(Fraction(0))

    return res


def check_inverse(poly: Polynomial) -> bool:
    dif_int = differentiate(integrate(poly))
    int_dif = integrate(differentiate(poly))

    if len(dif_int) != len(int_dif) != len(poly):
        return False

    for i in range(0, len(poly) - 1):
        if dif_int[i] != poly[i] or int_dif[i] != poly[i]:
            return False

    if dif_int[-1] != poly[-1]:
        return False

    return True
