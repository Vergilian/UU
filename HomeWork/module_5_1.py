class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print(f"{new_floor} этаж - Такого этажа не существует, максимальный - {self.number_of_floor} этаж")
        else:
            count = 0
            while new_floor!=count:
                count += 1
                print(count, "Этаж")
                if new_floor == count:
                    print('Мы приехали на выбранный Вами этаж \n' )



Urban = House('Урбан', 18)
Teacher_house = House('Учительский домик', 2)
Urban.go_to(5)
Teacher_house.go_to(10)