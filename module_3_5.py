def get_multiplied_digits(number):
    str_number = str(abs(number))
    first = int(str_number[0])
    if len(str_number) < 2:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(-40203) #целые - это ещё и отрицательные числа
print(result)