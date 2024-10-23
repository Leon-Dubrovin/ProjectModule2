n = int(input('Введите число на первом камне (3-20): '))
num_list = []
result =''
for i in range(1, n // 2 + 1):
    for j in range(i + 1, n):
        if i + j > n: break
        if n % (i + j) == 0:
            num_list.append(str(i))
            num_list.append(str(j))
result = result.join(num_list)
print(result)