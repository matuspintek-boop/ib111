def updated(x: int, y: int, cells: set[tuple[int, int]]) -> bool:
    count = 0
    alive = (x, y) in cells

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx or dy:
                count += (x + dx, y + dy) in cells

    return count in {2, 3} if alive else count == 3


def life(cells: set[tuple[int, int]], n: int) \
        -> set[tuple[int, int]]:
    if n == 0:
        return cells

    todo = set()
    ngen = set()

    for x, y in cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                todo.add((x + dx, y + dy))

    for x, y in todo:
        if updated(x, y, cells):
            ngen.add((x, y))

    return life(ngen, n - 1)
