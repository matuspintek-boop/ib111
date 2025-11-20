

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None
        self.id = 0

    def idstr(self) -> str:
        return ('₀₁₂₃₄₅₆₇₈₉'[self.id // 10] +
                '₀₁₂₃₄₅₆₇₈₉'[self.id % 10])


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return NotImplemented
        a = self.head
        b = other.head
        while a or b:
            if a is None or b is None:
                return False
            if a.id != b.id:
                return False
            if a.value != b.value:
                return False
            a = a.next
            b = b.next
        return True

    def __repr__(self) -> str:
        out = '(head)'
        ptr = self.head

        while ptr is not None:
            out += ' → ' + str(ptr.value) + ptr.idstr()
            ptr = ptr.next
        return out


def build_linked(nums: list[int]) -> LinkedList:
    head = Node(0)
    tail = head

    for i, v in enumerate(nums):
        tail.next = Node(v)
        tail = tail.next
        tail.id = i % 100

    result = LinkedList()
    result.head = head.next
    return result


def shuffle(permutation: list[int], linked: LinkedList) -> None:
    if permutation == []:
        return

    nodes_in_order: list[Node | None] = \
        [None for _ in permutation]

    curr_idx = 0
    curr_node = linked.head

    while curr_node is not None:
        nodes_in_order[permutation[curr_idx]] = curr_node
        curr_node = curr_node.next
        curr_idx += 1

    linked.head = nodes_in_order[0]
    last_added = linked.head

    for i in range(1, len(nodes_in_order)):
        if last_added is None:
            break

        last_added.next = nodes_in_order[i]
        last_added = last_added.next

    if last_added is not None:
        last_added.next = None


def sanity(student: to_test, replace: to_test) -> None:
    replace(Node)
    replace(LinkedList)
    student.main()
