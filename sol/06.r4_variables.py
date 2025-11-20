def operation(operator: str, left: int, right: int) -> int:
    if operator == "+":
        return left + right
    return left * right


def evaluate(expr: dict[str, tuple[str, str, str]],
             const: dict[str, int], var: str) -> int:
    results = {}
    stack = [var]

    while stack:
        top = stack[-1]
        if top in const:
            results[top] = const[top]
        elif top in expr:
            op, left, right = expr[top]
            if left in results and right in results:
                results[top] = operation(op, results[left],
                                         results[right])
            else:
                stack.append(left)
                stack.append(right)
                continue  # do not pop
        else:
            results[top] = 0
        stack.pop()

    return results[var]
