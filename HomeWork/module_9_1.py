def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        try:
            if not all(isinstance(string, (int, float)) for string in int_list):
                raise ValueError("Используйте список чисел")
            result[i.__name__] = i(int_list)
        except ValueError as e:
            return e
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func(["6, 20, 15, 9"], max, min))
