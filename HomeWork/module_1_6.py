my_dict = {'Denis': 1998, 'Anton': 2000}
print("Dict:", my_dict)
print("Existing value:", my_dict['Denis'])
my_dict['Max'] = [2001, 2002]
print("Not existing value:", my_dict['Max'])
my_dict.update({'Alexandra': 2002,
                'Venera': 2003})
key = my_dict.pop('Anton')
print("Deleted value:", key)
print("Modified dictionary", my_dict)
print() #вставил пустую строчку для разделения в консоли

my_set = {1, 2, 3, 1, 'Job', 1, 'Job', 2, 'Job'}
print("Set:", my_set)
my_set.add('Done')
my_set.add(5)
my_set.remove(3)
print("Modified set", my_set)