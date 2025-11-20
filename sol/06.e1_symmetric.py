def is_symmetric(relation: set[tuple[int, int]]) -> bool:
    for a, b in relation:
        if (b, a) not in relation:
            return False
    return True
