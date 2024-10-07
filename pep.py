# import this

while True:
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print("Число чётное")
        continue
    else:
        print("Число нечётное")
    print("не забыли")
print("Я за циклом")