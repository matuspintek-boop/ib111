class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = self


class CircularList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.end: Node | None = None

    def insert(self, value: int) -> None:
        new_head = Node(value)
        if self.head is None:
            self.end = new_head
        else:
            assert self.end is not None
            new_head.next = self.head
            self.end.next = new_head
        self.head = new_head

    def last(self) -> Node | None:
        return self.end

    def split_by_value(self, value: int) -> 'CircularList':
        assert self.head is not None
        it = self.head
        while it.value != value:
            it = it.next
        return self.split_by_node(it)

    def split_by_node(self, node: Node) -> 'CircularList':
        assert self.head is not None
        assert self.end is not None

        if node == self.end:
            return CircularList()

        new_list = CircularList()
        new_list.head = node.next
        new_list.end = self.end
        new_list.end.next = new_list.head

        node.next = self.head
        self.end = node

        return new_list
