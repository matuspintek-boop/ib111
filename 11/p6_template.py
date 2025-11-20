from ib111 import week_11  # noqa


# Napište čistou funkci, která na základě daného vzoru vytvoří
# množinu všech odpovídajících řetězců. Vzor je tvořený
# alfanumerickými znaky a navíc může obsahovat hranaté závorky –
# znaky ‹[› a ‹]›. Mezi těmito závorkami může stát libovolný počet
# přípustných znaků (krom samotných hranatých závorek) a na daném
# místě se ve výsledném řetězci může nacházet libovolný z těchto
# znaků. Například vzor ‹a[bc]d› reprezentuje řetězce ‹abd› a ‹acd›.


def expansion(already_have: set[str], plus: str) -> set[str]:
    output: set[str] = set()

    for string in already_have:
        output.add(string+plus)
    return output


def resolve_template(template: str) -> set[str]:
    output: set[str] = set()
    if len(template.replace("[", "").replace("]", "")) == 0:
        return set()
    else:
        output.add("")

    work_list: list[str] = list(template)
    variability: bool = False
    index = 0
    while index < len(work_list):
        if work_list[index] == "[":
            variability = True
        elif work_list[index] == "]":
            variability = False
        elif variability:
            new_output: set[str] = set()
            while work_list[index] != "]":
                new_output.update(expansion(output, work_list[index]))
                index += 1
                variability = False
            output = new_output
        else:
            new_output_: set[str] = set()
            new_output_.update(expansion(output, work_list[index]))
            output = new_output_
        index += 1

    return output


def main() -> None:
    assert resolve_template("[]") == set()

    assert resolve_template("a") == {"a"}
    assert resolve_template("[abc]") == {"a", "b", "c"}
    assert resolve_template("a[bc]d") == {"abd", "acd"}
    assert resolve_template("[Hh]ello, [Ww]orld") \
        == {"Hello, World", "Hello, world", "hello, World", "hello, world"}
    assert resolve_template("[ab]x[cd]y[ef]") \
        == {"axcye", "axcyf", "axdye", "axdyf",
            "bxcye", "bxcyf", "bxdye", "bxdyf"}
    assert resolve_template("[abc]abc[ef]") \
        == {"aabce", "aabcf", "babce", "babcf", "cabce", "cabcf"}
    assert resolve_template("[ab][a][b][c][d]") \
        == {"aabcd", "babcd"}


if __name__ == '__main__':
    main()
