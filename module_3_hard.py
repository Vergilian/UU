data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum = 0

def calculate_structure_sum(*arqs):
    global total_sum
    for item in arqs:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item,(list, set, tuple)):
            for sub_item1 in item:
                calculate_structure_sum(sub_item1)
        elif isinstance(item, dict):
            for sub_item2 in item.values():
                calculate_structure_sum(sub_item2)
            for sub_item3 in item.keys():
                calculate_structure_sum(sub_item3)
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)
