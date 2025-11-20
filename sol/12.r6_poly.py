def poly_to_str(coefs: list[int]) -> str:
    result = ""

    for i in range(len(coefs)):
        curr_term = term_to_string(coefs[i], len(coefs) - i - 1, i != 0)
        if curr_term != "":
            result += curr_term + " "

    if result == "":
        return "0"

    return result.rstrip()


def digit_to_int(digits: str, table: dict[str, int]) -> int:
    number = 0

    for curr in digits:
        number *= 10
        number += table[curr]

    return number


def int_to_digits(num: int, digits: str) -> str:
    out = ''
    while num > 0:
        out = digits[num % 10] + out
        num //= 10
    return out


def upper_index_to_int(idx: str) -> int:
    return digit_to_int(idx,
                        {"⁰": 0, "¹": 1, "²": 2, "³": 3, "⁴": 4,
                         "⁵": 5, "⁶": 6, "⁷": 7, "⁸": 8, "⁹": 9})


def coef_to_int(coef: str) -> int:
    table = {"+": 0, "-": 0,
             "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
             "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    sign = -1 if coef[0] == '-' else 1
    return sign * digit_to_int(coef, table)


def coef_exp_from_term(term: str) -> tuple[int, int]:
    parts = term.split("x")
    if len(parts) == 1:
        return (coef_to_int(term), 0)

    coef, power = parts
    if coef == "+" or coef == "-":
        coef += "1"

    if power == "":
        return (coef_to_int(coef), 1)

    return (coef_to_int(coef), upper_index_to_int(power))


def get_terms_from_str_poly(poly: str) -> list[str]:
    tokens = poly.split()
    terms = []

    start = 0
    if len(tokens) % 2 == 1:
        terms.append(tokens[0])
        start = 1

    for i in range(start, len(tokens), 2):
        terms.append(tokens[i] + tokens[i + 1])

    return terms


def str_to_poly(poly: str) -> list[int]:
    terms = get_terms_from_str_poly(poly)

    coefs = []
    last_exp = -1

    for term in terms:
        coef, exp = coef_exp_from_term(term)

        while last_exp > exp + 1:
            coefs.append(0)
            last_exp -= 1

        coefs.append(coef)
        last_exp = exp

    while last_exp != 0:
        coefs.append(0)
        last_exp -= 1

    return coefs


def int_to_upper_index(num: int) -> str:
    return int_to_digits(num, "⁰¹²³⁴⁵⁶⁷⁸⁹")


def term_to_string(coef: int, power: int, sign: bool) -> str:
    if coef == 0:
        return ""

    term = "- " if coef < 0 else ("+ " if sign else "")
    coef = abs(coef)

    if coef != 1:
        term += int_to_digits(coef, "0123456789")

    if power >= 1:
        term += "x"

    if power > 1:
        term += int_to_upper_index(power)

    return term
