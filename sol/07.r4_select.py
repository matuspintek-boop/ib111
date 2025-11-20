

def select(indices: list[int], linked: LinkedList) -> LinkedList:
    current = linked.head
    index = 0
    result = LinkedList()
    last = None

    for pick in indices:
        while index < pick:
            index += 1
            assert current is not None
            current = current.next

        assert current is not None

        node = Node(current.value)

        if last is None:
            result.head = node
        else:
            last.next = node

        last = node

    return result
