

def evaluate_bdd(bdd: BDD, true_vars: set[str]) -> bool:
    if bdd.val == "1":
        return True
    if bdd.val == "0":
        return False

    assert bdd.left is not None and bdd.right is not None

    next_bdd = bdd.right if bdd.val in true_vars else bdd.left
    return evaluate_bdd(next_bdd, true_vars)
