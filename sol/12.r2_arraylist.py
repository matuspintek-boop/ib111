class Node:
    def __init__(self) -> None:
        self.data: list[int] = []
        self.next: 'Node | None' = None


class ArrayList:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = Node()
            self.tail = self.head

        assert self.tail is not None

        if len(self.tail.data) == self.capacity:
            node = Node()
            self.tail.next = node
            self.tail = node

        self.tail.data.append(value)

    def delete(self, value: int) -> None:
        node = self.head
        prev = None
        while node is not None:
            if value in node.data:
                if len(node.data) == 1:
                    self.unlink(prev, node)
                else:
                    node.data.pop(node.data.index(value))
                return
            prev = node
            node = node.next

    def unlink(self, prev: Node | None, node: Node) -> None:
        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next
        if node == self.tail:
            self.tail = prev

    def compact(self) -> None:
        node = self.head
        while node is not None:
            self.move_to(node)  # fill current node
            node = node.next

    def move_to(self, node: Node) -> None:
        fit = self.capacity - len(node.data)
        if node.next is None or fit == 0:
            return

        if len(node.next.data) <= fit:
            node.data.extend(node.next.data)
            self.unlink(node, node.next)
            self.move_to(node)  # need more data → tail-recurse
        else:
            trimmed = []
            for idx, val in enumerate(node.next.data):
                if idx < fit:
                    node.data.append(val)
                else:
                    trimmed.append(val)
            node.next.data = trimmed
