def is_allowed(num: int, allowed: set[int]) -> bool:
    while num > 0:
        if num % 10 not in allowed:
            return False
        num //= 10
    return True


def wormhole(nums: list[int], allowed: set[int]) -> list[int]:
    return [num for num in nums if is_allowed(num, allowed)]
