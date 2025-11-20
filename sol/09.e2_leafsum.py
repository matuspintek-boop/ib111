

def sum_leaves(node: Tree) -> int:
    if len(node.children) == 0:
        return node.value
    return sum([sum_leaves(child) for child in node.children])
