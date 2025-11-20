from ib111 import week_05  # noqa

# Známky studentů z jednoho předmětu jsou uloženy ve slovníku, kde
# klíčem je UČO studenta a hodnotou je známka zadaná jako písmeno.
# Možná hodnocení jsou 'A' až 'F', dále, 'N', 'P', 'X', 'Z' a '-'.

# Napište čistou funkci ‹modus›, jejímž vstupem bude slovník známek
# a výstupem bude jejich modus, tedy nejčastější hodnota.
# Předpokládejte, že známek se stejnou četností může být více, takže
# funkce bude vždy vracet množinu známek, a to i v případě, že je
# nejčastější hodnota určena jednoznačně. V případě, že je vstupní
# slovník prázdný, bude výstupem prázdná množina.


def modus(marks: dict[int, str]) -> set[str]:
    outuput: set[str] = set()
    max_: int = 0
    data: dict[str, int] = {}

    for mark in marks.values():
        if mark not in data:
            data[mark] = 0
        data[mark] += 1

        if data[mark] > max_:
            max_ = data[mark]

    for key, value in data.items():
        if value == max_:
            outuput.add(key)

    return outuput

# Dále napište predikát ‹check›, který ověří, že známky jsou
# smysluplné, tedy že odpovídají buďto předmětu ukončenému zkouškou
# (známky 'A' - 'F', nebo 'X'), kolokviem (známky 'P' nebo 'N'),
# anebo zápočtem (známky 'Z' nebo 'N'). Hodnocení '-' je možné
# u jakéhokoliv způsobu hodnocení. Klasifikované zápočty
# neuvažujeme.


def check(marks: dict[int, str]) -> bool:

    possible: dict[str, set[str]] = {
        "exam": set(['A', 'B', 'C', 'D', 'E', 'F', 'X', '-']),
        "colocvium": set(['P', 'N', '-']),
        "zap": set(['Z', 'N', '-'])
    }

    candidates: set[str] = set(possible.keys())

    for mark in marks.values():
        to_delete = []
        for key in candidates:
            if mark not in possible[key]:
                to_delete.append(key)

        for key in to_delete:
            candidates.remove(key)

    return len(candidates) > 0


def main() -> None:
    assert modus({}) == set()
    assert modus({100000: 'P'}) == {'P'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A'}) == {'A'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'}) \
           == {'A', 'B'}
    assert check({})
    assert check({100000: 'P'})
    assert check({100000: '-'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'})
    assert not check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'N'})
    assert not check({100000: 'P', 100001: 'N', 100002: 'Z', 100003: '-'})


if __name__ == "__main__":
    main()
