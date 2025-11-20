def bisect(fun, low, high, eps):
    while True:
        mid = (low + high) / 2
        x = fun(mid)
        if abs(x) < eps:
            return mid

        if fun(low) * x < 0:
            high = mid
        else:
            low = mid
