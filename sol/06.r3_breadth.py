

def breadth(tree: Tree) -> int:
    maximal = 1
    row = [1]

    while row:
        next_row = []
        for node in row:
            for succ in tree[node]:
                next_row.append(succ)
        if len(next_row) > maximal:
            maximal = len(next_row)
        row = next_row

    return maximal
