

def tree_to_expr(node: Tree) -> str:
    if node.left is None or node.right is None:
        return node.value

    return "".join(["(", tree_to_expr(node.left),
                    " ", node.value,
                    " ", tree_to_expr(node.right),
                    ")"])
