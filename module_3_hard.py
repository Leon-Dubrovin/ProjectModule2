def calculate_structure_sum(*items):
    result = 0
    for item in items:
        if any((isinstance(item, list), isinstance(item, tuple), isinstance(item, set))):
            result += calculate_structure_sum(*item)
        elif isinstance(item, dict):
            result += calculate_structure_sum(*item.keys()) + calculate_structure_sum(*item.values())
        elif any((isinstance(item, int), isinstance(item, float), isinstance(item, bool))):
            result += item
        elif isinstance(item, str):
            result += len(item)
    return result

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)