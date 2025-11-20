from ib111 import week_08  # noqa


# † Třída ‹LinkedList› reprezentuje zřetězený seznam, se kterým
# budete pracovat. Uzly tohoto seznamu mají atribut ‹next›, ke
# kterému můžete libovolně přistupovat a měnit ho a metodu
# ‹compare›, která srovná hodnoty uložené ve dvou uzlech. K samotným
# hodnotám přímo přistupovat nesmíte. Volání ‹a.compare(b)› vrátí
# (-1, 0, 1) je-li hodnota v uzlu ‹a› (menší, stejná, větší) než
# hodnota v uzlu ‹b›.  První uzel je uložen v atributu ‹head›.
# Třídy LinkedList a Node nijak nemodifikujte.

class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None


# Napište funkci ‹merge›, která spojí 2 vzestupně seřazené zřetězené
# seznamy do jediného seřazeného seznamu. Funkce nevytváří nové
# uzly, pouze přepojuje ukazatele ‹next› stávajících uzlů z obou
# seznamů. Seznamy lze spojit v lineárním čase.

def merge(left: LinkedList, right: LinkedList) -> LinkedList:
    output: LinkedList = LinkedList()
    output_current: Node | None = None
    output.head = output_current

    current_left: Node | None = left.head
    current_right: Node | None = right.head

    while current_left is not None or current_right is not None:

        if current_left is None:
            if output_current is not None:
                output_current.next = current_right
            else:
                output.head = current_right
            current_right = None

        elif current_right is None:
            if output_current is not None:
                output_current.next = current_left
            else:
                output.head = current_left
            current_left = None

        elif current_right.compare(current_left) >= 0:
            if output_current is None:
                output_current = current_left
                output.head = output_current
            else:
                output_current.next = current_left
                output_current = output_current.next
            current_left = current_left.next

        else:  # current_right.compare(current_left) < 0:
            if output_current is None:
                output_current = current_right
                output.head = output_current
            else:
                output_current.next = current_right
                output_current = output_current.next
            current_right = current_right.next

    return output


def main() -> None:
    test_merge([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6])
    test_merge([2, 2, 4, 4], [1, 1, 3, 3], [1, 1, 2, 2, 3, 3, 4, 4])
    test_merge([], [1, 2, 3, 4], [1, 2, 3, 4])
    test_merge([1, 2, 3, 4], [], [1, 2, 3, 4])
    test_merge([], [], [])


def from_list(items: list[int]) -> LinkedList:
    ll = LinkedList()
    curr: Node | None = None
    for val in items:
        node = Node(val)
        if curr is None:
            ll.head = node
        else:
            curr.next = node
        curr = node
    return ll


def test_merge(left: list[int], right: list[int], expect: list[int]) -> None:
    result = merge(from_list(left), from_list(right))
    r_item = result.head
    e_item = from_list(expect).head
    while r_item is not None:
        assert e_item is not None
        assert r_item.compare(e_item) == 0
        r_item = r_item.next
        e_item = e_item.next
    assert e_item is None


class Node:

    def __init__(self, init_val: int) -> None:
        self.__value = init_val
        self.next: Node | None = None

    def compare(self, other: 'Node') -> int:
        if self.__value > other.__value:
            return 1
        if self.__value < other.__value:
            return -1
        return 0


if __name__ == "__main__":
    main()
