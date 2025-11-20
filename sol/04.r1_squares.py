def find_slope(points: list[tuple[float, float]],
               avg_x: float, avg_y: float) -> float | None:
    dividend: float = 0
    divisor: float = 0

    for i, (x, y) in enumerate(points):
        dividend += ((x - avg_x) * (y - avg_y))
        divisor += (x - avg_x) ** 2

    if divisor == 0:
        return None

    return dividend / divisor


def find_intercept(avg_x: float, avg_y: float, beta: float) -> float:
    return avg_y - beta * avg_x


def regress_vectors(x: list[float], y: list[float]) \
        -> tuple[float, float] | None:
    return regress_points([(x[i], y[i]) for i in range(len(x))])


def regress_points(points: list[tuple[float, float]]) \
        -> tuple[float, float] | None:
    avg_x = sum([x for x, _ in points]) / len(points)
    avg_y = sum([y for _, y in points]) / len(points)

    slope = find_slope(points, avg_x, avg_y)

    if slope is None:
        return None

    intercept = find_intercept(avg_x, avg_y, slope)
    return (intercept, slope)


def residuals_vectors(x: list[float], y: list[float],
                      alpha: float, beta: float) -> list[float]:
    points = [(x[i], y[i]) for i in range(len(x))]
    return residuals_points(points, alpha, beta)


def residuals_points(points: list[tuple[float, float]],
                     alpha: float, beta: float) -> list[float]:
    res = []
    for i, (x, y) in enumerate(points):
        res.append(abs(y - beta * x - alpha))
    return res
