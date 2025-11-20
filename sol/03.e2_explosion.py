from math import sqrt


def distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def survivors(objects, center, radius):
    out = []
    for obj in objects:
        if distance(obj, center) > radius:
            out.append(obj)
    return out
