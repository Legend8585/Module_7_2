def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for index, string in enumerate(strings, start=1):
        position = file.tell()
        file.write(string + '\n')
        strings_positions[(index, position)] = string
    file.close()
    return strings_positions


##Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
