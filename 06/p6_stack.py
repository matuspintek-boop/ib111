from ib111 import week_06  # noqa


# Čistá funkce ‹valid_stack_ops› dostane na vstupu dva seznamy
# ‹pushed›, ‹popped› a rozhodne, jestli tyto seznamy mohly být
# výsledkem posloupnosti operací «push» a «pop» nad zásobníkem,
# který je na začátku prázdný. (Seznam ‹pushed› má odpovídat pořadí,
# v němž byly prvky vkládány operací «push»; seznam ‹popped› pořadí,
# v němž byly prvky odebírány operací «pop».) Předpokládejte, že se
# ani v jednom vstupním seznamu neopakují stejné prvky.
#
# Příklady:
#
# Pro vstup ‹([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])› má být výsledkem
# ‹True›, protože existuje posloupnost operací «push 1», «push 2»,
# «push 3», «push 4», «pop» (vrátí 4), «push 5», «pop» (vrátí 5),
# «pop» (vrátí 3), «pop» (vrátí 2), «pop» (vrátí 1).
#
# Pro vstup ‹([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])› má být výsledkem
# ‹False›, protože neexistuje žádná posloupnost operací «push»
# a «pop», která by odpovídala těmto seznamům.

def valid_stack_ops(pushed: list[int], popped: list[int]) -> bool:
    # early exit for not possible case
    if len(pushed) < len(popped):
        return False

    # early exit for entry = [] []
    if pushed == []:
        return True
    # list containing pushed values
    pushed_copy = [pushed[0]]

    # idex last pushed into pushed_copy from pushed
    pushed_index = 0

    # popped values in reverse order
    popped_copy = popped.copy()
    popped_copy.reverse()

    # variable that reflexed if there are values
    # left to be pushed into pushed copy
    pushed_enabled = True

    # variable that defines change in length of lists
    pop_done = False

    while len(popped_copy) > 0 and pushed_index < len(pushed):
        if len(pushed_copy) > 0 and pushed_copy[-1] == popped_copy[-1]:
            pushed_copy.pop()
            popped_copy.pop()
            pop_done = True

        elif pushed_enabled:
            pushed_copy.append(pushed[pushed_index + 1])
            pushed_index += 1
            if pushed_index == len(pushed) - 1:
                pushed_enabled = False

        else:
            if not pop_done and not pushed_enabled:
                return False
            pop_done = False

    return True


def main() -> None:
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    assert valid_stack_ops(pushed, popped)
    assert pushed == [1, 2, 3, 4, 5]
    assert popped == [4, 5, 3, 2, 1]

    assert not valid_stack_ops([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
    assert valid_stack_ops([1, 2, 3, 4, 5], [3, 5])
    assert valid_stack_ops([], [])
    assert not valid_stack_ops([], [1])

    pushed = [1, 2, 3, 4, 5]
    popped = [3, 5, 2]
    assert not valid_stack_ops(pushed, popped)
    assert pushed == [1, 2, 3, 4, 5]
    assert popped == [3, 5, 2]

    assert valid_stack_ops(
        [42, 17, 1729, 1337, 1, 2, 3, 10, 11, 12, 1000, 0, -17, 7],
        [17, 1337, 1729, 3, 2, 12, 11, -17, 0, 1000, 7],
    )


if __name__ == '__main__':
    main()
