first = input('Введите 1 число:\n')
second = input('Введите 2 число:\n')
third = input('Введите 3 число:\n')
if third == second and third == first and first == second:
    print(3)
elif first == third or first == second or second == third:
    print(2)
else:
    print(0)