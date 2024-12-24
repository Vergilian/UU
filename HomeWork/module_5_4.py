class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название дома: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __eq__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other.number_of_floor, int) and isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



urban = House('Урбан', 10)
print(House.houses_history)
teacher_house = House('Учительский домик', 20)
print(House.houses_history)
forester = House('Дом лесника', 30)
print(House.houses_history)

# Удаление объектов
del teacher_house
del forester

print(House.houses_history)
