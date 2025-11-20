# Toto je tzv. naivní řešení. Lepší uvidíme na třetí přednášce.

def gcd(x1, x2):
    if x1 == 0 or x2 == 0:
        return max(abs(x1), abs(x2))

    curr_divisor = min(abs(x1), abs(x2))
    while curr_divisor > 0:
        if x1 % curr_divisor == 0 and x2 % curr_divisor == 0:
            return curr_divisor
        curr_divisor -= 1
