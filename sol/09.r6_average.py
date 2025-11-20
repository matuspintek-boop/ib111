

def average_branch_len(tree: Tree | None) -> float:
    if tree is None:
        return 0
    branch_lens = all_branch_lens(tree)
    return float(sum(branch_lens)) / len(branch_lens)


def all_branch_lens(tree: Tree) -> list[int]:
    res: list[int] = []
    all_branch_lens_rec(tree, 1, res)
    return res


def all_branch_lens_rec(tree: Tree,
                        curr_depth: int, lens: list[int]) -> None:
    if tree.left is None and tree.right is None:
        lens.append(curr_depth)
        return

    for child in [tree.left, tree.right]:
        if child is not None:
            all_branch_lens_rec(child, curr_depth + 1, lens)
