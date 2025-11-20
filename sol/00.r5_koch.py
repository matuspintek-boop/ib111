from turtle import forward, left, right


def koch_segment(size, iteration):
    if iteration == 0:
        forward(size)
    else:
        iter_size = size / 3
        koch_segment(iter_size, iteration - 1)
        left(60)
        koch_segment(iter_size, iteration - 1)
        right(120)
        koch_segment(iter_size, iteration - 1)
        left(60)
        koch_segment(iter_size, iteration - 1)


def koch_snowflake(size, iterations):
    for i in range(3):
        koch_segment(size, iterations)
        right(120)
