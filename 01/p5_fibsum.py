from ib111 import week_01  # noqa


# Napište funkci, která spočítá sumu prvních ‹n› «sudých» členů
# Fibonacciho posloupnosti (tj. členů, které jsou sudé, nikoliv
# těch, které mají sudé indexy). Například volání ‹fibsum(3) = 44 =
# 2 + 8 + 34›.

def fibsum(n):
    counter = 0
    sum_ = 0
    current = 1
    previous = 1
    while counter < n:
        stack = current
        current += previous
        previous = stack
        if current % 2 == 0:
            sum_ += current
            counter += 1
    return sum_


def main():
    assert fibsum(0) == 0
    assert fibsum(1) == 2
    assert fibsum(2) == 10
    assert fibsum(3) == 44
    assert fibsum(4) == 188
    assert fibsum(5) == 798
    assert fibsum(10) == 1089154


if __name__ == "__main__":
    main()
