from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, \
    penup, pendown, speed


# Napište proceduru, která nakreslí „tunel“ – sekvenci soustředných
# čtverců, kde vnější má stranu délky ‹size› a každý další je
# o ‹step› jednotek menší.

def draw_rectangle(size):
    for i in range(4):
        forward(size)
        left(90)

def tunnel(size, step):
    while size > 0:
        draw_rectangle(size)
        penup()
        forward(step/float(2))
        left(90)
        forward(step/float(2))
        right(90)
        pendown()
        size -= step



def main():
    speed(5)
    tunnel(150, 30)
    done()


if __name__ == "__main__":
    main()
