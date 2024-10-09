import random


def get_random():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    any = random.choice(numbers)
    return any


first_field = get_random()
print("Первое поле камня:", first_field)
pair = []

for i in range(1, 21):
    for j in range(1, 21):
        if i >= j:
            continue
        elif first_field % (i + j) == 0:
            # pair.append([i, j]) Удобный вид пар
            pair.extend([i, j])

print("Result key: ", *pair, sep='')
