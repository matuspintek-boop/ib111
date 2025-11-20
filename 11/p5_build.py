from ib111 import week_11  # noqa


# † V tomto příkladu budeme pracovat s n-árními stromy, které nemají
# v uzlech žádné hodnoty (mají pouze stromovou strukturu).
# Třídu Tree nijak nemodifikujte.

class Tree:
    def __init__(self) -> None:
        self.children: list[Tree] = []


# Napište (čistou) funkci, které na základě dobře uzávorkovaného
# řetězce tvořeného pouze znaky ‹(› a ‹)› vybuduje instanci výše
# popsaného stromu, a to tak, že každý pár závorek reprezentuje
# jeden uzel, a jejich obsah reprezentuje podstrom, který v tomto
# uzlu začíná. Ve vstupním řetězci bude vždy alespoň jeden pár
# závorek.

def build_tree(brackets: str) -> Tree:

    bracket_list: list[str] = list(brackets)
    bracket_list.pop()
    bracket_list.pop(0)
    brackets_trimmed: str = "".join(bracket_list)

    data: list[Tree] = [Tree()]
    current_index = 0
    for bracket in brackets_trimmed:
        if bracket == "(":
            current_tree: Tree = Tree()
            data[current_index].children.append(current_tree)
            current_index += 1
            if current_index < len(data):
                data[current_index] = current_tree
            else:
                data.append(current_tree)
        else:
            current_index -= 1
    return data[0]


def main() -> None:
    t2 = build_tree("()")
    assert len(t2.children) == 0

    t1 = build_tree("(()())")
    assert len(t1.children) == 2

    t3 = build_tree("(()(()())(()))")
    assert len(t3.children) == 3
    assert len(t3.children[0].children) == 0
    assert len(t3.children[1].children) == 2
    assert len(t3.children[1].children[0].children) == 0
    assert len(t3.children[1].children[1].children) == 0
    assert len(t3.children[2].children) == 1
    assert len(t3.children[2].children[0].children) == 0

    t4 = build_tree("(((())))")
    assert len(t4.children) == 1
    assert len(t4.children[0].children) == 1
    assert len(t4.children[0].children[0].children) == 1
    assert len(t4.children[0].children[0].children[0].children) == 0


if __name__ == '__main__':
    main()
