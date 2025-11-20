

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None

    # XXX the visited set is 'any' (masqueraded as to_test) because
    # for reasons unknown, python explodes on set[int] here (though
    # it works elsewhere)

    def to_str(self, visited: to_test) -> str:
        out = str(self.value)
        if id(self) in visited:
            out += " (loop)"
        elif self.next is not None:
            out += ' → ' + self.next.to_str(visited | {id(self)})
        return out

    def __repr__(self) -> str:
        return self.to_str(set())

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.value == other.value and self.next == other.next
        else:
            return NotImplemented


class SortedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def insert(self, value: int) -> None:
        node = Node(value)

        it: Node | None = self.head
        prev = None
        while it is not None and it.value < value:
            prev = it
            it = it.next

        node.next = it
        if prev is not None:
            prev.next = node
        else:
            self.head = node

    def get_greatest_in(self, value: int, dist: int) -> int | None:
        out = None
        it = self.head
        while it is not None and it.value < value:
            it = it.next
        while it is not None and it.value <= value + dist:
            out = it.value
            it = it.next
        return out

    def __eq__(self, other: object) -> bool:
        if hasattr(other, 'head'):
            return self.head == getattr(other, 'head')
        else:
            return NotImplemented

    def __repr__(self) -> str:
        return '(head) → ' + repr(self.head)


def make_tests(list_type: to_test) -> to_test:
    def construct_linked(values: list[int]) -> to_test:
        result = list_type()
        for v in values:
            result.insert(v)
        return result

    def construct_and_get(values: list[int], value: int,
                          dist: nat) -> int | None:
        lst = construct_linked(values)
        return lst.get_greatest_in(value, dist)

    return construct_linked, construct_and_get


def sanity(student: to_test, replace: to_test) -> None:
    replace(Node)
    student.main()
