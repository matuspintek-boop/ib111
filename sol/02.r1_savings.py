from math import floor


def apply_interest(amount, rate):
    return floor(amount + amount * rate / 100.0)


def savings_years(savings, interest_rate, inflation, withdraw):
    years = 0
    while savings >= withdraw:
        savings -= withdraw
        savings = apply_interest(savings, interest_rate)
        withdraw = apply_interest(withdraw, inflation)
        years += 1
    return years


# Alternative version (interest as integers in tenths of percents).

def apply_interest_alt(amount, rate):
    return amount * (1000 + rate) // 1000
