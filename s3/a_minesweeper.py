from ib111 import week_09  # noqa

# I v této sadě si naprogramujete jednu hru, a bude jí «Minesweeper¹».
# Naše verze bude trochu modifikovaná, zejména kliknutí na minu nebude nutně
# znamenat konec hry, ale způsobí výbuch, který poškodí část herní plochy.
# (Každá mina bude mít přiřazenu tzv. „sílu“ určující, kolik okolních políček
# bude zasaženo.)
#
# ¹ ‹https://en.wikipedia.org/wiki/Minesweeper_(video_game)›
#
# Abyste si hru mohli vyzkoušet (poté, co implementujete všechny níže
# uvedené metody), máte opět k dispozici soubor ‹game_minesweeper.py›, který
# spusťte ze stejného adresáře, jako je soubor s vaším řešením. Na začátku
# souboru jsou konstanty, jejichž úpravou můžete změnit velikost herní
# plochy, počet min a vzhled hry.
#
# Třída ‹Minesweeper›, kterou máte implementovat, reprezentuje stav hry,
# tj. obsah herní plochy, pozici min a aktuální skóre. Interní detaily jsou
# na vás, nicméně očekáváme, že objekty této třídy budou mít alespoň tyto
# dva atributy:
#
# • ‹status› – 2D seznam (seznam seznamů – řádků) reprezentující stav hry;
#   prvky vnitřních seznamů jsou těchto hodnot (UNKNOWN, EXPLODED, DESTROYED
#   jsou celočíselné konstanty definované níže):
#    ◦ ‹UNKNOWN› představuje dosud neodkryté (a nezničené) políčko,
#    ◦ ‹EXPLODED› představuje vybuchlou minu,
#    ◦ ‹DESTROYED› představuje políčko zničené výbuchem,
#    ◦ ‹0› až ‹8› představují odkryté políčko s informací o počtu
#      sousedících min.
# • ‹score› – počet bodů (celé číslo); body se udělují takto:
#    ◦ +1 bod za každé odkrytí políčka bez miny,
#    ◦ -10 bodů za každou vybuchlou minu.
#
# Kliknutí na některé políčko herní plochy bude zpracováno metodou ‹uncover›
# (viz níže). Je-li již políčko odkryté nebo zničené výbuchem, tato metoda
# nemá žádný efekt. V opačném případě se políčko odkryje a nastane jeden
# z těchto případů:
#
# • Je-li na tomto políčku mina, vybuchne a všechna políčka ve vzdálenosti
#   menší nebo rovné síle miny budou zničena. Pokud na některém z těchto
#   políček byla dosud nevybuchlá mina, rovněž vybuchne. To může zničit
#   další políčka a tento proces se může opakovat (i vícekrát).
#   Políčka, kde vybuchla mina, se označí stavem ‹EXPLODED›, ostatní zničená
#   políčka se označí stavem ‹DESTROYED›. (Stav ‹EXPLODED› na herní ploše
#   zůstává a nemění se na ‹DESTROYED› ani při dalším výbuchu.)
# • V opačném případě se stav políčka nastaví na ‹0› až ‹8› podle počtu
#   min (i těch už vybuchlých) v bezprostředním okolí. Je-li stav ‹0›,
#   odkryjí se všechna okolní políčka, což se opět může vícekrát opakovat.
#
# Pojmy „okolí“ a „vzdálenost“ zde chápeme ve všech osmi směrech (tedy
# i diagonálně). Vybuchlá mina se silou 1 tedy zničí až osm políček,
# vybuchlá mina se silou 2 zničí až 24 políček atd.
#
# Souřadnice zde používáme opět ve tvaru (sloupec, řádek), přičemž sloupce
# číslujeme od 0 zleva a řádky od 0 shora.
#
# Hodnoty níže uvedených konstant neměňte.

Position = tuple[int, int]

UNKNOWN = -1
EXPLODED = -2
DESTROYED = -3


class Minesweeper:

    # Po inicializaci mají být všechna pole herní plochy neodkrytá,
    # herní plocha má mít rozměry zadané parametry ‹width› a ‹height›
    # a skóre má být 0. Parametr ‹mines› určuje pozici min (klíče slovníku)
    # a jejich sílu (hodnoty slovníku). Slovník ‹mines› nijak nemodifikujte.
    # Pokud si ho hodláte někam uložit, tak buďto zařiďte, aby se ani později
    # nemodifikoval, nebo si vytvořte jeho kopii.

    def __init__(self, width: int, height: int,
                 mines: dict[Position, int]):
        self.status = [[UNKNOWN for i in range(width)] for i in range(height)]
        self.mines: dict[Position, int] = mines.copy()
        self.score: int = 0
        self.explosion_id: int = 0

    # Metoda ‹uncover› provede odkrytí políčka dle popisu výše a případně
    # upraví skóre. Předpokládejte, že souřadnice jsou validní (tj. v rozsahu
    # herní plochy).

    def explosion(self, x: int, y: int, power: int) -> None:
        self.status[y][x] = EXPLODED
        for u in range(-power, power + 1):
            for v in range(-power, power + 1):
                if -1 < x-u < len(self.status[0]) \
                   and -1 < y - v < len(self.status):
                    if self.mines.get((x-u, y-v), -1) > - 1:
                        self.score -= 10
                        self.explosion(x-u, y-v,
                                       self.mines.pop((x - u, y - v)))
                    if self.status[y-v][x-u] != EXPLODED:
                        self.status[y-v][x-u] = DESTROYED
        return

    def scan_surroundings(self, x: int, y: int) -> int:
        mines_found: int = 0
        for u in range(-1, 2):
            for v in range(-1, 2):
                if -1 < x-u < len(self.status[0]) \
                   and -1 < y - v < len(self.status):
                    if self.status[y-v][x-u] == EXPLODED \
                       or self.mines.get((x - u, y - v), -1) > -1:
                        mines_found += 1
        return mines_found

    def uncover(self, x: int, y: int) -> None:
        if self.mines.get((x, y), -1) > -1:
            self.score -= 10
            self.explosion(x, y, self.mines.pop((x, y)))

        elif self.status[y][x] == UNKNOWN:
            self.status[y][x] = self.scan_surroundings(x, y)
            self.score += 1
            if self.status[y][x] == 0:
                for u in range(-1, 2):
                    for v in range(-1, 2):
                        if -1 < x-u < len(self.status[0]) \
                           and -1 < y - v < len(self.status):
                            self.uncover(x-u, y-v)


def main() -> None:
    # for nicer matrices below
    U, E, D = UNKNOWN, EXPLODED, DESTROYED
    mines = {(2, 2): 5, (4, 5): 1, (6, 1): 0, (6, 3): 1, (6, 4): 3}

    ms = Minesweeper(8, 6, mines)
    assert ms.score == 0
    assert ms.status == [
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
    ]

    ms.uncover(1, 1)
    assert ms.score == 1
    assert ms.status == [
        [U, U, U, U, U, U, U, U],
        [U, 1, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
        [U, U, U, U, U, U, U, U],
    ]

    ms.uncover(0, 0)
    assert ms.score == 33
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, 1, 1, 3, U, U],
        [0, 0, 0, 1, U, U, U, U],
    ]

    ms.uncover(5, 4)
    assert ms.score == 33
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, 1, 1, 3, U, U],
        [0, 0, 0, 1, U, U, U, U],
    ]

    ms.uncover(4, 5)
    assert ms.score == 23
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, D, D, D, U, U],
        [0, 0, 0, D, E, D, U, U],
    ]

    ms.uncover(5, 5)
    assert ms.score == 23
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, 1, 0, 1, U, U],
        [0, 1, U, 1, 0, 2, U, U],
        [0, 1, 1, 1, 0, 2, U, U],
        [0, 0, 0, D, D, D, U, U],
        [0, 0, 0, D, E, D, U, U],
    ]

    ms.uncover(6, 3)
    assert ms.score == -7
    assert ms.status == [
        [0, 0, 0, 0, 0, 1, U, U],
        [0, 1, 1, D, D, D, E, D],
        [0, 1, U, D, D, D, D, D],
        [0, 1, 1, D, D, D, E, D],
        [0, 0, 0, D, D, D, E, D],
        [0, 0, 0, D, E, D, D, D],
    ]

    assert mines == {(2, 2): 5, (4, 5): 1, (6, 1): 0, (6, 3): 1, (6, 4): 3}

    mines = {(0, 1): 0, (1, 0): 0, (1, 1): 0}
    ms = Minesweeper(3, 3, mines)
    ms.uncover(0, 0)
    ms.uncover(0, 0)
    ms.uncover(0, 2)
    ms.uncover(2, 0)
    ms.uncover(2, 2)
    ms.uncover(1, 1)
    assert ms.score == -6
    assert ms.status == [[3, -1, 2], [-1, -2, -1], [2, -1, 1]]


if __name__ == '__main__':
    main()
