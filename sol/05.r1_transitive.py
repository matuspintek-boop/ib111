def is_transitive(relation: set[tuple[int, int]]) -> bool:
    for a, b in relation:
        for b_prime, c in relation:
            if b == b_prime and (a, c) not in relation:
                return False
    return True
