

from ib111 import week_03  # noqa


# V tomto domácím úkolu si naprogramujete zjednodušenou variantu hry «2048¹».
# Na rozdíl od původní hry budeme uvažovat jen jednorozměrný hrací plán,
# tj. jeden řádek.
#
# ¹ ‹https://play2048.co/›
#
# Hrací plán budeme reprezentovat pomocí seznamu nezáporných celých čísel;
# nuly budou představovat prázdná místa.
# Například seznam ‹[2, 0, 0, 2, 4, 8, 0]› reprezentuje následující situaci:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │ 2 │   │   │ 2 │ 4 │ 8 │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#
# Základním krokem hry je posun doleva nebo doprava. Při posunu se všechna
# čísla „sesypou“ v zadaném směru, přičemž dvojice stejných číslic se sečtou.
# Posunem doleva se tedy uvedený seznam změní na ‹[4, 4, 8, 0, 0, 0, 0]›.
#
# Abyste si hru mohli vyzkoušet (poté, co úlohu vyřešíte), je vám k dispozici
# soubor ‹game_2048.py›, který vložte do stejného adresáře, jako je soubor
# s vaším řešením, případně jej upravte dle komentářů na jeho začátku
# a spusťte. Hra se ovládá šipkami doleva a doprava, ‹R› hru resetuje
# a ‹Q› ukončí.
#
# Napište proceduru ‹slide›, která provede posun řádku reprezentovaného
# seznamem ‹row›, a to buď doleva (pokud má parametr ‹to_left› hodnotu ‹True›)
# nebo doprava (pokud má parametr ‹to_left› hodnotu ‹False›). Procedura přímo
# modifikuje parametr ‹row› a vrací ‹True›, pokud posunem došlo k nějaké
# změně; v opačném případě vrací ‹False›.

# function for finding first non zero value in row
def find_first(left, row):
    if left:
        for i in range(0, len(row)):
            if row[i] != 0:
                return i
        return -1
    else:
        for i in range(len(row) - 1, - 1, -1):
            if row[i] != 0:
                return i
        return -1
# finding non zero neightbour of index, depending on direction
# neightbour to the right or to the left
# if none found returning -1


def find_neightbour(right, row, current):
    if right:
        i = current + 1
        while i < len(row):
            if row[i] != 0:
                return i
            i += 1
        return -1
    else:
        i = current - 1
        while i > -1:
            if row[i] != 0:
                return i
            i -= 1
        return -1


def next_item(index, toleft):
    if toleft:
        return index+1
    else:
        return index-1


def slide(row, to_left):
    # default values
    output = False
    i = find_first(to_left, row)
    # early exit for empty row
    if i == -1:
        return output

    # setting first found non zero value
    # on start
    if to_left:
        if i > 0:
            output = True
            row[0] = row[i]
            row[i] = 0
            i = 0

    if not to_left:
        if i < len(row) - 1:
            output = True
            row[-1] = row[i]
            row[i] = 0
            i = len(row) - 1

    # variable for already added value, stop bubbling
    merged = False

    # cycle that goes throught all items in row
    while i != -1:
        # getting neightbour index, if none found returning false
        neightbour = find_neightbour(to_left, row, i)
        if neightbour == -1:
            return output

        # next index to be worked with
        next = next_item(i, to_left)

        # if numbers will be moved, output is true
        if to_left and neightbour > next or not to_left and neightbour < next:
            output = True

        # merging two items with same values
        if row[neightbour] == row[i] and not merged:
            row[i] += row[neightbour]
            row[neightbour] = 0
            output = True
            merged = True

        # if we have two different values,
        # moving them closer to the side
        elif merged or row[neightbour] != row[i]:
            merged = False
            value = row[neightbour]
            row[neightbour] = 0
            row[next] = value
            if to_left:
                i += 1
            if not to_left:
                i -= 1

    return output


def main():
    row = [0, 2, 2, 0]
    assert slide(row, True)
    assert row == [4, 0, 0, 0]

    row = [2, 2, 2, 2, 2]
    assert slide(row, False)
    assert row == [0, 0, 2, 4, 4]

    row = [2, 0, 0, 2, 4, 2, 2, 2]
    assert slide(row, True)
    assert row == [4, 4, 4, 2, 0, 0, 0, 0]

    row = [3, 0, 6, 3, 3, 3, 6, 0, 6]
    assert slide(row, False)
    assert row == [0, 0, 0, 0, 3, 6, 3, 6, 12]

    row = [16, 8, 4, 2, 0, 0, 0]
    assert not slide(row, True)
    assert row == [16, 8, 4, 2, 0, 0, 0]


if __name__ == '__main__':
    main()
