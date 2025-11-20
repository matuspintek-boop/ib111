

def satisfiable(phi: Formula) -> bool:
    for clause in phi:
        curr_vars: dict[str, bool] = {}
        contradiction_found = False

        for variable, value in clause:
            if curr_vars.get(variable, value) != value:
                contradiction_found = True
            curr_vars[variable] = value

        if not contradiction_found:
            return True

    return False
