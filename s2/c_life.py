from ib111 import week_06  # noqa

# Hru «Life¹» už jste si možná zkusili implementovat v rámci rozšířených
# příkladů ve čtvrté kapitole. V tomto úkolu budete implementovat její trochu
# složitější verzi. Místo jednoho života budeme simulovat souboj dvou různých
# organismů (modré a oranžové buňky), pozice po úmrtí buňky bude po několik kol
# neobyvatelná a budeme mít trochu jiná pravidla pro to, kdy buňky vznikají
# a zanikají. Kromě toho bude náš „svět“ neomezený a bude obsahovat „otrávené“
# oblasti, kde žádné buňky nepřežijí.
#
# ¹ ‹https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life›
#
# Stav „světa“ je dán slovníkem, jehož klíči jsou 2D souřadnice a hodnotami
# čísla od jedné do šesti:
#
# • číslo 1 reprezentuje živou modrou buňku,
# • číslo 2 reprezentuje živou oranžovou buňku,
# • čísla 3 až 6 reprezentují pozici, kde dříve zemřela buňka
#   (čím větší číslo, tím víc času od úmrtí buňky uplynulo).
#
# Pozice, které nejsou obsaženy ve slovníku, jsou prázdné.

Position = tuple[int, int]
State = dict[Position, int]

# Stejně jako ve hře Life, za «okolí» pozice považujeme sousední pozice
# ve všech osmi směrech, tj. včetně diagonál.
# Základní pravidla vývoje světa jsou následující:
#
# • Pokud jsou v okolí prázdné pozice přesně tři živé buňky, vznikne zde
#   v dalším kole buňka nová. Barva nové buňky odpovídá většinové barvě
#   živých buněk v okolí. Jinak zůstává prázdná pozice prázdnou.
# • Pokud je v okolí živé buňky tři až pět živých buněk (na barvě nezáleží),
#   buňka zůstane živou i v dalším kole (a ponechá si svou barvu).
#   V opačném případě buňka umře a stav této pozice v dalším kole bude číslo 3.
# • Má-li pozice stav 3 až 5, pak v dalším kole bude mít stav o jedna větší.
# • Má-li pozice stav 6, v dalším kole bude prázdná.
#
# „Otrávené“ pozice jsou zadány extra (jako množina) a mění základní pravidla
# tak, že živé buňky na otrávených pozicích «a v jejich okolí» vždy zemřou
# a na těchto pozicích (otrávených a jejich okolí) nikdy nevzniknou nové buňky.


# Napište čistou funkci ‹evolve›, která dostane počáteční stav světa ‹initial›,
# množinu „otrávených“ pozic ‹poison› a počet kol ‹generations› a vrátí stav
# světa po zadaném počtu kol.

<<<<<<< HEAD

def tupple_sum(tuplpex: tuple[int, int]) -> int:
    x, y = tuplpex
    return x + y


def get_surroundings(position: Position,
                     remove_initial: bool) -> set[Position]:
    x, y = position
    output: set[Position] = set()
    for i in [x, x+1, x-1]:
        for j in [y, y+1, y-1]:
            output.add((i, j))
    if remove_initial:
        output.remove((x, y))
    return output


def evolve(initial: State, poison: set[Position],
           generations: int) -> State:

    poisoned: dict[Position, bool] = {}

    initial_ = initial.copy()

    for position in poison:
        for position_ in get_surroundings(position, False):
            poisoned[position_] = True

    for i in range(generations):
        to_pop: list[Position] = []
        candidates: dict[Position, tuple[int, int]] = {}
        for key, value in initial_.items():

            if value == 6:
                to_pop.append(key)
                continue

            if value > 2 and value < 6:
                initial_[key] += 1
                continue

            for position_ in get_surroundings(key, True):

                blue, orange = candidates.get(position_, (0, 0))

                if value == 1:
                    blue += 1

                if value == 2:
                    orange += 1

                candidates[position_] = (blue, orange)

            if i < 1:
                if poisoned.get(key):
                    initial_[key] = 3
                    continue

        # print("--------------------candidates-----------------------------")
        # print(candidates)
        for key, value in initial_.items():
            if value >= 3:
                candidates.pop(key, None)
                continue
            if value < 3:
                if key not in candidates:
                    initial_[key] = 3
                    continue
                if tupple_sum(candidates[key]) < 3 or \
                   tupple_sum(candidates[key]) > 5:
                    initial_[key] = 3
                    candidates.pop(key, 0)

        for position_ in to_pop:
            initial_.pop(position_)

        for key, val in candidates.items():
            # print(key, val)
            # print(key not in initial_, key not in poisoned, tupple_sum(val))
            if tupple_sum(val) == 3 and key not in initial_ \
               and key not in poisoned:
                # print(key)
                blue, orange = val
                initial_[key] = 1
                if orange > blue:
                    initial_[key] = 2

    # print ("------------------------output_state--------------------")
    # print(initial_)
    return initial_
=======
def evolve(initial: State, poison: set[Position],
           generations: int) -> State:
    pass
>>>>>>> 86de6671d8cfc1b1bdd86d787b45ccf64db353e7


# Pro vizualizaci je vám k dispozici soubor ‹game_life.py›, který vložte do
# stejného adresáře, jako je soubor s vaším řešením. Na začátku tohoto souboru
# jsou parametry vizualizace (velikost buněk, rychlost vývoje), popis
# iniciálního stavu světa a „otrávených“ pozic. Vizualizace volá vaši funkci
# evolve s parametrem ‹generations› vždy nastaveným na 1.


def main() -> None:
    square = {(3, 3): 1, (3, 4): 2, (4, 4): 1, (4, 3): 2}

    assert evolve(square, set(), 1000) == square

    assert evolve(square, {(3, 3)}, 1) \
        == {(3, 3): 3, (3, 4): 3, (4, 4): 3, (4, 3): 3}

    planet = {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1,
              (0, -1): 1, (1, -1): 3}

    assert evolve(planet, set(), 10) \
        == {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1,
            (2, 0): 6, (1, -1): 5, (0, -1): 4, (-1, 0): 3, (-1, 1): 1}

    ship = {(0, 0): 1, (0, 1): 1,
            (-1, 0): 1, (-1, 1): 1, (-1, 2): 1,
            (1, 0): 1, (1, 1): 1, (1, 2): 1,
            (-2, 2): 1, (2, 2): 1}

    assert evolve(ship, {(2, -19)}, 42) \
        == {(-1, -17): 6, (1, -17): 6, (0, -18): 6, (-2, -17): 6}

    assert evolve(ship, {(3, -19)}, 1000) \
        == {(-1, -496): 5, (0, -497): 6, (-1, -497): 3, (1, -497): 5,
            (0, -498): 4, (-2, -496): 6, (-1, -498): 1, (1, -498): 3,
            (0, -499): 1, (-2, -497): 4, (-1, -499): 1, (1, -499): 1,
            (0, -500): 1, (-2, -498): 1, (-1, -500): 1, (1, -500): 1}

    collision = {(-20, -2): 1, (-20, -1): 1, (-19, -1): 1, (-18, -1): 1,
                 (-19, 0): 1, (-18, 0): 1, (-20, 1): 1, (-19, 1): 1,
                 (-18, 1): 1, (-20, 2): 1, (21, -2): 2, (21, -1): 2,
                 (20, -1): 2, (19, -1): 2, (20, 0): 2, (19, 0): 2,
                 (21, 1): 2, (20, 1): 2, (19, 1): 2, (21, 2): 2}

    assert evolve(collision, set(), 46) == {}

    collision_out_of_sync = {
        (-20, -2): 1, (-20, -1): 1, (-19, -1): 1, (-18, -1): 1, (-19, 0): 1,
        (-18, 0): 1, (-20, 1): 1, (-19, 1): 1, (-18, 1): 1, (-20, 2): 1,
        (21, -1): 2, (20, -1): 2, (19, -1): 2, (19, 0): 2, (18, 0): 2,
        (21, 1): 2, (20, 1): 2, (19, 1): 2
    }

    assert evolve(collision_out_of_sync, set(), 100) \
        == {(-1, -3): 1, (-1, 3): 1, (-1, -4): 1, (-1, 4): 1,
            (-2, -4): 1, (-2, -3): 1, (-2, 3): 1, (-2, 4): 1}

<<<<<<< HEAD
    state = {(967, 967): 1, (963, 963): 6, (964, 965): 2, (966, 966): 5,
             (968, 964): 2, (968, 966): 2, (968, 963): 2, (963, 965): 1,
             (964, 966): 1, (964, 967): 4, (966, 967): 2, (966, 964): 1}
    poison = {(963, 967), (964, 963), (965, 963), (965, 964), (966, 968)}
    assert (965, 966) in evolve(state, poison, 1)

=======
>>>>>>> 86de6671d8cfc1b1bdd86d787b45ccf64db353e7

if __name__ == '__main__':
    main()
