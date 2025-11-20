from ib111 import week_01  # noqa


# Uvažujme hru čtyř hráčů s následujícími pravidly:
#
# • herní plán je jednorozměrný, s neomezenou délkou a vyznačeným startovním
#   políčkem;
# • každý hráč má jednu figurku, na začátku umístěnou na startovním políčku;
# • hráči střídavě hází kostkou a posunují své figurky o hozené číslo;
# • pokud by hráčova figurka měla vstoupit na políčko obsazené figurkou
#   jiného hráče, tato figurka je „vykopnuta“ (jako v Člověče, nezlob se)
#   zpět na start.
#
# Situaci na herním plánu budeme reprezentovat pomocí nezáporného celého čísla
# tak, že jeho zápis v pětkové soustavě reprezentuje obsazenost jednotlivých
# políček bez startovního políčka. Číslice 0 reprezentuje prázdné políčko,
# číslice 1–4 pak reprezentují obsazenost figurkou konkrétního hráče. Pohyb
# figurek přitom v pětkovém zápisu probíhá „zprava doleva“, tedy směrem od
# nižších řádů k vyšším.
#
# Příklady:
#
#  ┌───────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#  │start: 1234│   │   │   │   │   │   │   │   │   │   │   │ …
#  └───────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
#
# Všechny figurky jsou na startu – stav reprezentovaný číslem 0.
#
#  ┌───────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#  │start: 1 3 │   │ 2 │   │   │   │ 4 │   │   │   │   │   │ …
#  └───────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
#
# Figurky hráčů 1 a 3 jsou na startu, figurka hráče 2 je dvě políčka od startu,
# figurka hráče 4 je šest políček od startu. Tento stav je reprezentovaný
# číslem ⟦(400020)₅ = 4 · 5⁵ + 2 · 5¹ = 12510⟧.
#
#
# Napište čistou funkci ‹play›, která na plánu reprezentovaném číslem ‹arena›
# provede jeden tah hráče ‹player› o zadaný hod kostkou ‹throw› a vrátí
# číslo reprezentující nový stav hry.
#
# Předpokládejte, že ‹arena› je validní stav hry (tj. nezáporné celé číslo,
# v jehož pětkovém zápisu se objevuje každá z číslic 1–4 nejvýše jednou),
# že ‹player› je jedno z čísel 1, 2, 3, 4 a že ‹throw› je kladné celé číslo.
# (Nemusí být nijak shora omezené; předpokládejte, že máme kostky s různě
# velkými čísly.)

def play(arena, player, throw):
    # backupvariables for counting
    # record = 0 number for debugging

    # copies of arena
    arena_backup = arena
    arena_backup2 = arena

    # is current player in record yet {record = arena}
    player_playing = False
    length = -1  # length of arena
    player_i = 0  # player grade
    counter = throw

    # deleting from arena backup, finding if player is already playing
    # if yes, moving player upwards depending on current length of arena
    while arena_backup > 0:
        length += 1
        current = arena_backup % 5
        if player_playing:
            counter -= 1
            if counter == 0:
                arena -= current*5**length
        if current == player:
            player_playing = True
            player_i = length
        arena_backup //= 5
    if player_playing:
        arena -= player*5**(player_i)
        arena += player*5**(player_i + throw)

    # fix for situation when player is not playing
    # and pushes out other player after throw
    if not player_playing:
        arena += player*5**(throw - 1)
        for i in range(throw):
            current = arena_backup2 % 5
            arena_backup2 //= 5
        arena -= current*5**(throw - 1)

    return arena


def main():
    for p in range(1, 5):
        assert play(0, p, 1) == p

    assert play(11, 3, 3) == 86
    assert play(84770, 4, 5) == 147250
    assert play(84770, 3, 4) == 240645
    assert play(12510, 1, 2) == 12505


if __name__ == '__main__':
    main()
