

def is_heap(tree: Tree | None) -> bool:
    if tree is None:
        return True

    if not heap_property_check(tree):
        return False

    return is_heap(tree.left) and is_heap(tree.right)


def heap_property_check(node: Tree) -> bool:
    if node.left is not None and node.left.key > node.key:
        return False
    if node.right is not None and node.right.key > node.key:
        return False
    return True
