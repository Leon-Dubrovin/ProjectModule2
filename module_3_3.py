#1.Функция с параметрами по умолчанию
def print_params(a = 1, b = 'python', c = True):
    print(f'a = {a}, b = {b}, c = {c}')

print_params()
print_params(15,'sausages')
print_params(['spam', 'spamspam', 'spamspamspam'])
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров
values_list = ['eggs из списка', 42, (3.14, 2.71)]
values_dict = {'a':15.4, 'b':False, 'c':'spice из словаря'}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры
values_list_2 = [145, 'spam']
print_params(*values_list_2, 42)