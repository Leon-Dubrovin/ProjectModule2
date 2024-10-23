calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return tuple([len(string), string.upper(), string.lower()])
def is_contains(string, list_to_search):
    count_calls()
    list_lowcase = [x.lower() for x in list_to_search]
    return string.lower() in list_lowcase

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)