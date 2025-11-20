from ib111 import week_03  # noqa


# «Mankala¹» je souborné označení deskových her pro dva hráče, jejichž
# společným znakem je přemisťování kuliček (kamínků, pecek, apod.) mezi důlky.
# V tomto domácím úkolu si naprogramujete jednoduchou variantu takové hry –
# pravidla jsou inspirována hrou «Kalaha²», resp. jednou z jejích obměn.
#
# ¹ ‹https://en.wikipedia.org/wiki/Mancala›
# ² ‹https://en.wikipedia.org/wiki/Kalah›

# Hrací deska sestává z dvou řad menších důlků (jejich počet je parametrem
# hry, viz níže) a dvou větších důlků vlevo a vpravo. Vypadá tedy např. takto
# (počet menších důlků v každé řadě je zde šest):
#
#  ╭───────╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───────╮
#  │       ││ M ││ L ││ K ││ J ││ I ││ H ││       │
#  │   N   │╰───╯╰───╯╰───╯╰───╯╰───╯╰───╯│       │
#  │       │╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮│   G   │
#  │       ││ A ││ B ││ C ││ D ││ E ││ F ││       │
#  ╰───────╯╰───╯╰───╯╰───╯╰───╯╰───╯╰───╯╰───────╯
#
# Hru hrají dva hráči, kteří sedí proti sobě. Každému hráči patří menší
# důlky na jeho straně a větší důlek vpravo – tento větší důlek nazýváme
# hráčovou «bankou». Na začátku hry je v každém menším důlku předem určený
# počet kuliček (toto je druhý parametr hry), banky jsou prázdné. Hra probíhá
# po kolech, přičemž se hráči střídají. Průběh každého kola je následující:
#
# • Hráč si vybere jeden ze svých menších důlků, který obsahuje nějaké
#   kuličky. Pokud jsou všechny důlky hráče prázdné, hra končí (viz níže).
# • Hráč vezme všechny kuličky z vybraného důlku a začne je po jedné
#   rozdělovat do následujících důlků proti směru hodinových ručiček, včetně
#   svého banku, ale «ne do banku soupeře».
#   Pokud tedy např. spodní hráč vzal kuličky z důlku C, pak je bude postupně
#   rozdělovat do důlků D, E, F, G, H, I, J, K, L, M, A, B, C, atd., dokud
#   mu nějaké kuličky budou zbývat.
# • Pokud při rozdělování padla poslední kulička do prázdného menšího důlku
#   na straně aktuálního hráče «a jeho oponent má v protějším důlku nějaké
#   kuličky», sebere hráč svou poslední kuličku a «všechny» kuličky
#   v protějším důlku a přesune je do své banky.
# • Pokud při rozdělování padla poslední kulička do hráčovy banky, v dalším
#   kole hraje tentýž hráč znovu; v opačném případě se hráči vystřídají.
#
# Hra končí, když má hráč, který je na tahu, všechny menší důlky prázdné.
# Jeho protivník si pak přesune všechny kuličky ze svých menších důlků do své
# banky. Vyhrává ten hráč, který má v bance více kuliček.
#
# Hrací desku reprezentujeme pomocí dvou seznamů nezáporných celých čísel.
# Každý seznam představuje důlky jednoho z hráčů (postupně zleva doprava
# z hráčova pohledu), přičemž počet kuliček v bance hráče je posledním prvkem
# seznamu. Desce naznačené výše tedy odpovídají seznamy ‹[A, B, C, D, E, F, G]›
# a ‹[H, I, J, K, L, M, N]›.
#
# Abyste si hru mohli vyzkoušet (poté, co úlohu vyřešíte), je vám k dispozici
# soubor ‹game_mancala.py›, který vložte do stejného adresáře, jako je soubor
# s vaším řešením, případně jej upravte dle komentářů na jeho začátku
# a spusťte.  Kliknutím na jeden z důlků se provede tah, klávesa ‹R› hru
# resetuje a ‹Q› ukončí.
#
# Implementujte nejprve čistou funkci ‹init›, která vrátí dvojici seznamů
# reprezentujících hrací desku se ‹size› menšími důlky, v nichž je na začátku
# ‹start› kuliček. Banky obou hráčů jsou prázdné. Předpokládejte, že ‹size›
# i ‹start› jsou kladná celá čísla.

def init(size, start):
    playing_array = [start for i in range(size)]
    playing_array.append(0)
    return (playing_array, playing_array.copy())


# Dále napište proceduru ‹play›, která odehraje jedno kolo hry. Parametr
# ‹our› je seznam reprezentující stranu aktuálního hráče, parametr ‹their›
# je seznam reprezentující stranu protivníka. Předpokládejte, že tyto seznamy
# mají stejnou délku větší než 1 a že obsahují pouze nezáporná celá čísla.
# Parametr ‹position› (celé číslo) určuje, který důlek se má vybrat (0 je
# důlek nejvíce vlevo z pohledu hráče).
#
# Pokud je ‹position› mimo platný rozsah, procedura nic nemodifikuje a vrátí
# konstantu ‹INVALID_POSITION›. Pokud je ‹position› indexem prázdného důlku,
# procedura nic nemodifikuje a vrátí konstantu ‹EMPTY_POSITION›.
# Jinak procedura modifikuje seznamy dle pravidel hry a vrátí buď konstantu
# ‹PLAY_AGAIN› nebo ‹ROUND_OVER›, podle toho, jestli má aktuální hráč hrát
# znovu nebo už skončil. Tyto konstanty jsou už definovány; nijak je neměňte.

INVALID_POSITION = 0
EMPTY_POSITION = 1
ROUND_OVER = 2
PLAY_AGAIN = 3


def round_play(our, their, position):

    # defining needed variables
    length = len(our)
    counter = our[position]

    # setting value on position on 0
    our[position] = 0

    # this variable decides site on whic
    # the game is currently played
    current_our = True
    position += 1

    # repeating cycle till we have no "balls" left
    while counter > 0:
        if current_our:
            if position < length:
                our[position] += 1
            if position == length - 1 and counter > 1:
                position = -1
                current_our = False
        else:
            if position < length - 1:
                their[position] += 1
            if position == length - 2 and counter > 1:
                position = -1
                current_our = True
        counter -= 1

        # this section of code decides the return value
        if counter == 0:
            if position == length - 1:
                return PLAY_AGAIN
            if current_our and our[position] == 1 and their[-position - 2] > 0:
                our[-1] += our[position]
                our[-1] += their[-position - 2]
                our[position] = 0
                their[-position - 2] = 0
            return ROUND_OVER
        position += 1


def play(our, their, position):
    # early exit for wrong starting positions
    if position > len(our) - 2 or position < 0:
        return INVALID_POSITION
    if our[position] == 0:
        return EMPTY_POSITION

    output = round_play(our, their, position)
    return output


def main():
    # --- init ---

    assert init(6, 3) \
        == ([3, 3, 3, 3, 3, 3, 0], [3, 3, 3, 3, 3, 3, 0])

    assert init(9, 7) \
        == ([7, 7, 7, 7, 7, 7, 7, 7, 7, 0], [7, 7, 7, 7, 7, 7, 7, 7, 7, 0])

    # --- play ---

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, -1) == INVALID_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 0) == PLAY_AGAIN
    assert our == [0, 1, 7, 1]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 1) == EMPTY_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]

    our = [0, 4, 0]
    their = [0, 0, 0]

    assert play(our, their, 1) == ROUND_OVER
    assert our == [0, 0, 3]
    assert their == [1, 0, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 2) == ROUND_OVER
    assert our == [4, 0, 0, 6]
    assert their == [4, 0, 4, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 3) == INVALID_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]



our = [1, 0, 0]
their = [0, 0, 0]

assert play(our, their, 0) == ROUND_OVER
assert our == [0, 1, 0]
assert their == [0, 0, 0]


if __name__ == '__main__':
    main()
