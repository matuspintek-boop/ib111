class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


def maximum(num_list: LinkedList) -> int | None:
    node = num_list.head

    if node is None:
        return None

    max_val = node.value

    while node is not None:
        if node.value > max_val:
            max_val = node.value
        node = node.next
    return max_val
