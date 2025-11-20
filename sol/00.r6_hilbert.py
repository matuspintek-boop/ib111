from turtle import forward, left, right


def hilbert_helper(iterations, angle, size):
    if iterations == 0:
        return

    right(angle)
    hilbert_helper(iterations - 1, -angle, size)

    forward(size)
    left(angle)
    hilbert_helper(iterations - 1, angle, size)

    forward(size)
    hilbert_helper(iterations - 1, angle, size)

    left(angle)
    forward(size)
    hilbert_helper(iterations - 1, -angle, size)
    right(angle)


def shrink(iterations):
    if iterations == 1:
        return 1

    return 2 * shrink(iterations - 1) + 1


def hilbert(size, iterations):
    hilbert_helper(iterations, 90,
                   size / shrink(iterations))
