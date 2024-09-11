def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [2, 'string1', 3.45]
values_dict = {'a': 3, 'b': 'string2', 'c': 1.23}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
