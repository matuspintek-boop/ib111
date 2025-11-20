def slope(x: list[float], y: list[float], average_x: float, average_y: float) \
        -> float | None:
    dividend: float = 0
    divisor: float = 0

    for i in range(len(x)):
        dividend += ((x[i] - average_x) * (y[i] - average_y))
        divisor += (x[i] - average_x) ** 2

    if divisor == 0:
        return None

    return dividend / divisor


def deviations(x: list[float], y: list[float], alpha: float, beta: float) \
        -> list[float]:
    res: list[float] = []
    for i in range(len(x)):
        res.append(abs(y[i] - beta * x[i] - alpha))
    return res


def least_squares(x: list[float], y: list[float]) \
        -> tuple[float, float, list[float]] | None:
    average_x: float = float(sum(x)) / len(x)
    average_y: float = float(sum(y)) / len(y)

    beta: float | None = slope(x, y, average_x, average_y)
    if beta is None:
        return None

    alpha: float = average_y - beta * average_x

    return (alpha, beta, deviations(x, y, alpha, beta))


