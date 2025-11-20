from ib111 import week_04  # noqa


# V této úloze bude Vaším úkolem implementovat funkce pracující se
# seznamem pacientů ‹patients› u lékaře. Každý pacient má záznam
# (dvojici), který obsahuje jeho unikátní identifikátor a seznam
# návštěv s výsledky. Návštěva je reprezentovaná čtveřicí – rokem,
# kdy pacient navštívil lékaře, a naměřenými hodnotami: pulz,
# systolický a diastolický tlak. Seznam návštěv pacienta je
# uspořádaný vzestupně od nejstarší. Můžete předpokládat, že každý
# pacient má alespoň jeden záznam.

# Vaším prvním úkolem bude implementovat a otypovat funkci
# ‹missing_visits›, která zjistí, kteří pacienti nebyli na prohlídce
# od roku ‹year›. Jako výsledek vraťte seznam identifikátorů
# pacientů.

Patient_id = int
Visit = tuple[int, int, int, int]
Patient = tuple[Patient_id, list[Visit]]

Patients = list[Patient]


def missing_visits(year: int, patients: Patients) -> list[Patient_id]:
    output: list[Patient_id] = []
    for patient in patients:
        id, visits = patient
        last_visit = visits[-1]

        year_, _, _, _ = last_visit

        if year_ <= year:
            output.append(id)

    return output


# Dále napište a otypujte funkci ‹patient_reports›, která vrátí
# seznam zpráv o pacientech. Zpráva o pacientovi je čtveřice, která
# obsahuje záznam o jeho nejvyšším doposud naměřeném pulzu a pro
# každou měřenou hodnotu informaci, zda se měření dané hodnoty
# v jednotlivých letech konzistentně zvyšují (‹True› nebo ‹False›).

# Například zpráva o pacientovi ‹(1, [(2015, 91, 120, 80), (2018,
# 89, 125, 82), (2020, 93, 120, 88)])› je ‹(93, False, False,
# True)›.
Hightest_pulse = int
Value_increase = bool
Record = tuple[Hightest_pulse, Value_increase, Value_increase, Value_increase]


def patient_reports(patients: Patients) -> list[Record]:
    output: list[Record] = []

    for patient in patients:
        id, visits = patient

        hightest_pulse: Hightest_pulse = 0
        _, pulse, systol, diastol = (1111, 0, 0, 0)

        for visit in visits:
            _, c_pulse, c_systol, c_diastol = visit

            hightest_pulse = max(hightest_pulse, c_pulse)

            if c_pulse > pulse:
                pulse = c_pulse
            else:
                pulse = 1000

            if c_systol > systol:
                systol = c_systol
            else:
                systol = 1000

            if c_diastol > diastol:
                diastol = c_diastol
            else:
                diastol = 1000
        output.append((hightest_pulse, pulse != 1000,
                       systol != 1000, diastol != 1000))
    return output


def main() -> None:
    p1 = (0, [(2016, 102, 140, 95)])
    p2 = (1, [(2015, 91, 120, 80), (2018, 89, 125, 82),
              (2020, 93, 120, 88)])
    p3 = (2, [(2010, 73, 110, 70), (2015, 75, 112, 70),
              (2017, 76, 114, 71), (2019, 79, 116, 72)])
    p4 = (3, [(2016, 82, 115, 82), (2017, 83, 117, 80)])
    p5 = (4, [(2005, 81, 130, 90), (2007, 81, 130, 90),
              (2011, 80, 130, 90), (2013, 81, 130, 90),
              (2017, 82, 130, 90)])

    p6 = (5, [(2000, 74, 120, 80), (2011, 107, 142, 95),
              (2012, 94, 140, 97)])
    p7 = (6, [(2019, 101, 145, 95), (2020, 101, 145, 95)])

    patients = [p1, p2, p3, p4, p5]
    assert missing_visits(2017, patients) == [0, 3, 4]
    assert missing_visits(2016, patients) == [0]
    assert missing_visits(2000, patients) == []

    assert patient_reports(patients) == \
        [(102, True, True, True), (93, False, False, True),
         (79, True, True, False), (83, True, True, False),
         (82, False, False, False)]

    assert patient_reports([p6, p7]) == \
        [(107, False, False, True), (101, False, False, False)]


if __name__ == "__main__":
    main()
