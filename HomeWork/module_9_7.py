def is_prime(func):
    def wrapper(a, b, c):
        result_ = func(a, b, c)
        if result_ % 2 == 0 or result_ % 3 == 0:
            print('Составное')
        else:
            print('Простое')
        return result_
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
