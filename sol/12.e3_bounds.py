

def get_bounds(tree: Tree) -> tuple[int, int]:
    return get_bounds_rec(tree, tree.value, tree.value)


def get_bounds_rec(tree: Tree | None,
                   low: int, high: int) -> tuple[int, int]:

    if tree is None:
        return (low, high)

    low = min(tree.value, low)
    high = max(tree.value, high)
    low, high = get_bounds_rec(tree.left, low, high)
    return get_bounds_rec(tree.right, low, high)
