def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(3, 'hello')
print_params(4, 'hello', False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [13, 'Fire', [2,3,2]]
values_dict_ = {'a': 7,'b': 7,'c': 7}
print_params(*values_list)
print_params(**values_dict_)

values_list_2 = [8,"bingo"]
print_params(*values_list_2)
print_params(*values_list_2, 42)