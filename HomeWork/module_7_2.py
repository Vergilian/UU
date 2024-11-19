def custom_write(file_name, strings):
    strings_positions = {}
    count = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        count += 1
        start_num = file.tell()
        file.write(f'{i}\n')
        strings_positions[(count, start_num)] = i
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!',
    'Всегда welcome'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
