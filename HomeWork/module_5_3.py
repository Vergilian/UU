class House:
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


urban = House('Урбан', 10)
teacher_house = House('Учительский домик', 20)

print(urban)
print(teacher_house)

print(urban == teacher_house)  # __eq__

urban = urban + 10  # __add__
print(urban)
print(urban == teacher_house)

urban += 10  # __iadd__
print(urban)

teacher_house = 10 + teacher_house  # __radd__
print(teacher_house)

print(urban > teacher_house)  # __gt__
print(urban >= teacher_house)  # __ge__
print(urban < teacher_house)  # __lt__
print(urban <= teacher_house)  # __le__
print(urban != teacher_house)  # __ne__
