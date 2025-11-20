from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed
from math import sin, radians


# Implementujte proceduru ‹heartbeat›, která vykreslí stylizovanou
# křivku EKG. Parametr ‹iterations› udává počet tepů, které
# procedura vykreslí. Zbylé parametry zadávají amplitudu základního
# úderu a periodu slabšího úderu. Slabší úder má poloviční
# amplitudu.  Například při periodě 3 bude mít sníženou amplitudu
# každý třetí úder, počínaje prvním.

def draw_beat(amplitude, angle, halph):
    # length between beats
    forward_length = 2*amplitude

    # if periodic beat reduce amplitude
    if halph:
        amplitude = amplitude / float(2)
    
    # drawing
    left(angle)
    forward(amplitude/ sin(radians(angle)))
    right(90+angle)
    forward(amplitude*2)
    left(90+angle)
    forward(amplitude/ sin(radians(angle)))
    right(angle)

    forward(forward_length)

def heartbeat(amplitude, period, iterations):
    angle = 80
    for i in range(iterations):
        if (i+1) % period == 0:
            draw_beat(amplitude, angle, True)
        else:
            draw_beat(amplitude, angle, False)


def main():
    speed(4)
    heartbeat(30, 3, 5)
    done()


if __name__ == "__main__":
    main()
