
DIRS = {
    '←': (-1, 0),
    '→': (+1, 0),
    '↑': (0, +1),
    '↓': (0, -1),
}


def step(direction: str, pos: Position) -> Position:
    x, y = pos
    dx, dy = DIRS[direction]
    return (x + dx, y + dy)


def walk(path: str, pos: Position) -> Position:
    for direction in path:
        pos = step(direction, pos)
    return pos


def meet(path_1: str, path_2: str, pos_1: Position,
         pos_2: Position) -> Position | None:
    if pos_1 == pos_2:
        return pos_1

    for i in range(max(len(path_1), len(path_2))):
        if i < len(path_1):
            pos_1 = step(path_1[i], pos_1)
        if i < len(path_2):
            pos_2 = step(path_2[i], pos_2)
        if pos_1 == pos_2:
            return pos_1
    return None
