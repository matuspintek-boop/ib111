def has_overlap(a, b):
    (ax1, ay1), (ax2, ay2) = a
    (bx1, by1), (bx2, by2) = b
    return ax1 <= bx2 and ax2 >= bx1 and ay1 <= by2 and ay2 >= by1


def filter_overlapping(rectangles):
    out = []
    count = len(rectangles)
    for i in range(count):
        for j in range(count):
            if i != j and has_overlap(rectangles[i], rectangles[j]):
                out.append(rectangles[i])
                break
    return out
