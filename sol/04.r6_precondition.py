def precondition_1(x_0: int, y: int) -> bool:
    return y != 0 and x_0 % y == 0


def precondition_2(x_0: int, y_0: int) -> bool:
    return x_0 <= y_0 and (x_0 - y_0) % 2 == 0


def precondition_3(x: int, y: int) -> bool:
    return x > 0 and y < 0


def precondition_4(x_0: int, y: int) -> bool:
    return x_0 >= 0 and y > 0
