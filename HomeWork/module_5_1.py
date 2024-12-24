class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


Urban = House('Урбан', 18)
Teacher_house = House('Учительский домик', 2)
Urban.go_to(5)
Teacher_house.go_to(10)
