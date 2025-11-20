def slope(x, y, average_x, average_y):
    dividend = 0
    divisor = 0

    for i in range(len(x)):
        dividend += ((x[i] - average_x) * (y[i] - average_y))
        divisor += (x[i] - average_x) ** 2

    if divisor == 0:
        return None

    return dividend / divisor


def deviations(x, y, alpha, beta):
    res = []
    for i in range(len(x)):
        res.append(abs(y[i] - beta * x[i] - alpha))
    return res


def least_squares(x, y):
    average_x = float(sum(x)) / len(x)
    average_y = float(sum(y)) / len(y)

    beta = slope(x, y, average_x, average_y)
    if beta is None:
        return None

    alpha = average_y - beta * average_x

    return (alpha, beta, deviations(x, y, alpha, beta))
