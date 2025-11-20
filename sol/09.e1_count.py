

def count(tree: Tree | None) -> int:
    if tree is None:
        return 0

    return 1 + count(tree.left) + count(tree.right)
