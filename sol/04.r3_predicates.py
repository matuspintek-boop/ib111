# unconfuse ib111.py


def test_f_1() -> None:
    # ‹f_1(x, y)› právě když ‹fib(x) == y›
    assert f_1(1, 1)
    assert f_1(2, 1)
    assert f_1(3, 2)
    assert f_1(4, 3)
    assert f_1(5, 5)
    assert f_1(6, 8)
    assert not f_1(4, 2)


def test_f_2() -> None:
    # ‹f_2(x, y)› právě když ‹divisors(x) ≥ y›
    assert f_2(1, 1)
    assert f_2(2, 2)
    assert f_2(3, 2)
    assert f_2(12, 6)
    assert not f_2(12, 7)
    assert f_2(12, 5)


def test_f_3() -> None:
    # ‹f_3(x, y)› právě když ‹divisors(x) > divisors(y)›
    assert not f_3(1, 1)
    assert f_3(12, 13)
    assert not f_3(3, 2)
    assert f_3(12, 6)


def test_f_4() -> None:
    # ‹f_4(x, y)› právě když ‹y - 1› je počet prvočísel < ‹x›
    assert f_4(3, 2)
    assert f_4(5, 3)
    assert f_4(6, 4)
    assert f_4(7, 4)
    assert f_4(11, 5)
    assert f_4(12, 6)
    assert f_4(17, 7)


def test_f_5() -> None:
    # ‹f_5(x)› právě když je ‹x› base-7 palindrom
    assert f_5(6)
    assert f_5(1 * 7**3 + 2 * 7**2 + 2 * 7 + 1)
    assert f_5(1 * 7**4 + 2 * 7**3 + 7 ** 2 + 2 * 7 + 1)
    assert not f_5(1 * 7**4 + 3 * 7**3 + 7 ** 2 + 2 * 7 + 1)


def test_f_6() -> None:
    # ‹f_6(x, y)› právě když jsou ‹x›, ‹y› v binárním zápisu
    # zrcadlové obrazy
    assert f_6(0b1101, 0b1011)
    assert f_6(0b110001, 0b100011)
    assert f_6(0b1101001, 0b1001011)
    assert not f_6(0b101001, 0b1001011)
    assert not f_6(0b101, 0b111)


def test_f_7() -> None:
    # ‹f_7(x, y)› právě když je ‹y› počet různých prvočísel
    # v rozkladu ‹x›
    assert f_7(7, 1)
    assert f_7(14, 2)
    assert f_7(15, 2)
    assert f_7(30, 3)


def test_f_8() -> None:
    # ‹f_8(x, y, z)› právě když je ‹z› počet různých prvočísel
    # dělících ‹x› a zároveň ‹y›
    assert f_8(1, 1, 0)
    assert f_8(2, 4, 1)
    assert f_8(4, 2, 1)
    assert f_8(21, 14, 1)
    assert f_8(14, 28, 2)
    assert f_8(28, 28, 2)
    assert f_8(9, 12, 1)
    assert f_8(16, 12, 1)
    assert f_8(24, 12, 2)
    assert f_8(120, 60, 3)
    assert f_8(180, 60, 3)
    assert f_8(180, 120, 3)
