from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    for i, j in enumerate(strings, 1):
        curcor = file.tell()
        file.write(j + '\n')
        strings_positions[(i, curcor)] = j
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
