

def depth(tree: Tree | None) -> int:
    if tree is None:
        return 0

    return 1 + max(depth(tree.left), depth(tree.right))
