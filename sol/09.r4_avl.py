

def is_avl(tree: Tree | None) -> bool:
    ok, _ = is_avl_rec(tree)
    return ok


def is_avl_rec(tree: Tree | None) -> tuple[bool, int]:
    if tree is None:
        return (True, 0)

    l_avl, l_depth = is_avl_rec(tree.left)
    r_avl, r_depth = is_avl_rec(tree.right)

    return (l_avl and r_avl and abs(l_depth - r_depth) <= 1,
            max(l_depth, r_depth) + 1)
