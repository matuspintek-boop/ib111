

def flatten(to_flatten: NestedList) -> list[int]:
    flattened: list[int] = []
    for item in to_flatten:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened
