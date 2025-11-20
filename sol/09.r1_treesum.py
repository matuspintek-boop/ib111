

def sum_tree(node: Tree | None) -> int:
    if node is None:
        return 0
    return (node.value +
            sum_tree(node.first) +
            sum_tree(node.second) +
            sum_tree(node.third))
