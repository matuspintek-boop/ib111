from typing import Annotated


NestedList = list['int | NestedList']


def copy(self: int | NestedList) -> int | NestedList:
    if isinstance(self, int):
        return self
    else:
        return [copy(i) for i in self]


def nested_enum(idx: int) -> NestedList:
    items: NestedList = []
    for sub in list_enum(idx):
        sub, nest = divmod(sub, 2)
        if nest:
            items.append(nested_enum(sub))
        else:
            items.append(sub)
    return items


NestedListGen = Annotated[NestedList, nested_enum]


def flatten(to_flatten: NestedList, result: list[int]) -> list[int]:
    for item in to_flatten:
        if isinstance(item, int):
            result.append(item)
        else:
            flatten(item, result)
    return result


def fill(nested: NestedList, values: list[int], index: int) -> int:
    for i, item in enumerate(nested):
        if isinstance(item, int):
            nested[i] = values[index]
            index += 1
        else:
            index = fill(item, values, index)
    return index


def sort_nested(nested: NestedListGen) -> None:
    flat = flatten(nested, [])
    flat.sort()
    fill(nested, flat, 0)
