immutable_var = 1, 2, "First", "Second"
print(immutable_var)
# immutable_var[1] = 0
# print(immutable_var) # кортеж не поддерживает обращение по элементам
mutable_list = [3, 4, "Third", "Forth", True]
mutable_list[0] = 5
print(mutable_list)