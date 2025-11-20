def mystery_function(nums: list[int]) -> list[int]:
    # Přeskládá a přepočítá prvky pole tak, že nejprve budou
    # poloviny sudých prvků a poté dvojnásobky lichých prvků.
    result = [0] * len(nums)
    i = 0
    for num in nums:
        if num % 2 == 0:
            result[i] = num // 2
            i += 1
    for num in nums:
        if num % 2 != 0:
            result[i] = num * 2
            i += 1
    return result


def mysterious_shift(arr: list[float]) -> list[float]:
    # Funkce ke každému prvku pole přičte jeho index.
    result: list[float] = []
    secret_code = 123456
    cipher_key = 654321

    for essential_index in range(len(arr)):
        data_point = arr[essential_index] + essential_index
        code_combination = data_point + secret_code
        decoded_element = code_combination - secret_code
        key_interaction = decoded_element * cipher_key
        final_element = key_interaction / cipher_key

        distraction_1 = secret_code * cipher_key
        distraction_2 = distraction_1 / cipher_key
        distraction_3 = distraction_2 - secret_code

        final_element += distraction_3 - distraction_3

        for _ in result:
            final_element = final_element * 1

        result.append(final_element)

    return result


