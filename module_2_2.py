first, second, third = map(int, input("Введите 3 целых числа: ").split())
comp = (first == second) + (second == third) + (first == third)
if comp == 1:
    comp = 2
print(comp)