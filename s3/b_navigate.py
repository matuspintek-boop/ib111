from ib111 import week_10  # noqa

# Vrátíme se k robotovi, jehož pohyb jsme simulovali ve druhé sadě úkolů
# (‹b_robot›). Budeme mít opět stejný plán ve tvaru neomezené čtvercové sítě
# s čtvercovými dílky s nákresy ulic či křižovatek. Tentokrát ovšem dáme
# robotovi možnost se pohybovat libovolným směrem podle možností na
# aktuálním dílku.

Heading = int
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
Tile = set[Heading]
Position = tuple[int, int]
Plan = dict[Position, Tile]


# Implementujte čistou funkci ‹navigate›, která vrátí cestu, kterou se robot
# dostane ze zadané startovní do zadané cílové pozice na zadaném plánu.
# Pokud žádná taková cesta neexistuje, funkce vrátí ‹None›. Vrácená cesta
# je ve formě seznamu všech pozic, kterými robot projde od startovní do
# cílové pozice včetně. Předpokládejte, že plán je korektní, tj. splňuje
# predikát ‹is_correct› z úlohy ‹s2/b_robot›, a že zadané pozice jsou na
# některém z položených dílků.
#
# Doporučení: Použijte princip backtrackingu. Budete muset nějak zařídit, aby
# robot neběhal v kruzích (pak by vaše funkce nemusela skončit).

def find_way(plan: Plan, current_position: Position,
             goal: Position, visited: set[Position],
             road: list[Position]) -> list[Position]:
    if current_position in visited:
        return road
    else:
        visited.add(current_position)
        road.append(current_position)
    if current_position == goal:
        return road
    else:

        x, y = current_position
        for heading in plan[current_position]:
            if heading == 0:
                if goal == find_way(plan, (x, y - 1), goal, visited, road)[-1]:
                    return road
            elif heading == 1:
                if goal == find_way(plan, (x + 1, y), goal, visited, road)[-1]:
                    return road
            elif heading == 2:
                if goal == find_way(plan, (x, y + 1), goal, visited, road)[-1]:
                    return road
            elif heading == 3:
                if goal == find_way(plan, (x - 1, y), goal, visited, road)[-1]:
                    return road
        road.pop()
        return road


def navigate(plan: Plan, start: Position, goal: Position) \
        -> list[Position] | None:

    result: list[Position] = find_way(plan, start, goal, set(), [])

    if len(result) > 0:
        return result

    # for mypy to be happy
    return None


def main() -> None:
    plan = {(1, 1): {NORTH}, (1, 0): {SOUTH}, (2, 2): {EAST}, (3, 2): {WEST}}
    assert_correct_navigate(plan, (1, 1), (2, 2), False)
    assert_correct_navigate(plan, (1, 1), (1, 0), True)
    assert_correct_navigate(plan, (3, 2), (2, 2), True)

    plan = {
        (-2, -2): {EAST, SOUTH},
        (-1, -2): {EAST, WEST},
        (0, -2): {SOUTH, WEST},
        (-5, -1): {SOUTH},
        (-2, -1): {NORTH, SOUTH},
        (0, -1): {NORTH, SOUTH},
        (5, -1): {EAST, SOUTH},
        (6, -1): {SOUTH, WEST},
        (-5, 0): {NORTH, EAST, SOUTH},
        (-4, 0): {EAST, WEST},
        (-3, 0): {EAST, WEST},
        (-2, 0): {NORTH, EAST, WEST},
        (-1, 0): {EAST, WEST},
        (0, 0): {NORTH, EAST, SOUTH, WEST},
        (1, 0): {EAST, WEST},
        (2, 0): {EAST, SOUTH, WEST},
        (3, 0): {EAST, WEST},
        (4, 0): {EAST, WEST},
        (5, 0): {NORTH, EAST, WEST},
        (6, 0): {NORTH, WEST},
        (-5, 1): {NORTH},
        (0, 1): {NORTH, SOUTH},
        (2, 1): {NORTH, SOUTH},
        (-1, 2): {EAST},
        (0, 2): {NORTH, EAST, WEST},
        (1, 2): {EAST, WEST},
        (2, 2): {NORTH, WEST},
    }

    assert_correct_navigate(plan, (-5, -1), (-5, 1), True)
    assert_correct_navigate(plan, (-5, -1), (-1, 2), True)
    assert_correct_navigate(plan, (0, 0), (2, 2), True)

    plan[2, 0] = {WEST, SOUTH}
    plan[3, 0] = {EAST}

    assert_correct_navigate(plan, (3, 0), (6, -1), True)
    assert_correct_navigate(plan, (3, 0), (0, 0), False)
    assert_correct_navigate(plan, (-5, -1), (6, -1), False)


def assert_correct_navigate(plan: Plan, start: Position, goal: Position,
                            possible: bool) -> None:
    path = navigate(plan, start, goal)
    if possible:
        assert path is not None
        assert correct_path(plan, start, goal, path)
    else:
        assert path is None


def correct_path(plan: Plan, start: Position, goal: Position,
                 path: list[Position]) -> bool:
    if len(path) == 0 or path[0] != start or path[-1] != goal:
        return False

    dirs = {(0, -1): NORTH, (0, +1): SOUTH, (-1, 0): WEST, (+1, 0): EAST}

    lx, ly = path[0]
    for i in range(1, len(path)):
        x, y = path[i]
        if (x, y) not in plan:
            return False

        diff = x - lx, y - ly
        if dirs.get(diff) not in plan[lx, ly]:
            return False

        lx, ly = x, y

    return True


if __name__ == '__main__':
    main()
