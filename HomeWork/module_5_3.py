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
            print(f"{new_floor} этаж - Такого этажа не существует, максимальный - {self.number_of_floor} этаж \n")
        else:
            count = 0
            while new_floor != count:
                count += 1
                print(count, "Этаж")
                if new_floor == count:
                    print('Мы приехали на выбранный Вами этаж \n')


urban = House('Урбан', 10)
teacher_house = House('Учительский домик', 20)
# urban.go_to(5)
# teacher_house.go_to(10)

#
print(urban)
print(teacher_house)
# print(len(urban))
# print(len(teacher_house))


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
