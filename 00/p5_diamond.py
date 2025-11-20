from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed, delay


# Napište proceduru pro vykreslení stylizovaného diamantu. Tento se
# skládá z mnohoúhelníků, které jsou vůči sobě natočené o vhodně
# zvolený malý úhel (takový, aby byl výsledný obrazec pravidelný).
# Každý mnohoúhelník má ‹sides› stran o délce ‹length› pixelů.

def draw_part(sides, length):
    for i in range(sides):
        forward(length)
        right(360/float(sides))

def diamond(sides, length):
    angle = 30
    for i in range(360//angle):
        draw_part(sides, length)
        left(angle)


def main():
    speed(1)
    delay(0)
    diamond(12, 30)
    done()


if __name__ == "__main__":
    main()
