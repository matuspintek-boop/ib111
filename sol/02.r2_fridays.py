def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def days_per_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


def is_friday(day_of_week):
    return day_of_week == 4


def fridays(year, day_of_week):
    count = 0
    for month in range(1, 13):
        days = days_per_month(year, month)
        for day in range(1, days + 1):
            if is_friday(day_of_week) and day == 13:
                count += 1
            day_of_week = (day_of_week + 1) % 7
    return count
