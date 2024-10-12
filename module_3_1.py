calls = 0


def string_info(string):
    count_calls()
    tuple_0 = tuple([len(string), string.upper(), string.lower()])
    return tuple_0


def count_calls():
    global calls
    calls += 1
    return calls


def is_contains(name, list):
    result=0
    count_calls()

    for i in range(len(list)):
        if list[i].lower() == name.lower():
            result = True
            break
        else:
            result = False
    return result


print(string_info('Pytnon'))
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('one', ['One', 'Frr', 'fr']))
print(calls)
