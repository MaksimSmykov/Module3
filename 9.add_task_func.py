data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*structure):
    total_sum = 0
    if len(structure) == 0:
        return 0
    for arg in structure:
        if isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
            total_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            total_sum += calculate_structure_sum(*arg.items())
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, int) or isinstance(arg, float):
            total_sum += arg
        else:
            continue
    return total_sum

result = calculate_structure_sum(data_structure)
print('\n',result)