from time import struct_time
import output_notes as on


def search(dictionary):
    search_string = input(
        '\nПо какому критерию ведём поиск? Текст, дата или номер? ').strip().lower()
    if search_string in ('текст', 'по тексту', 'text', 'txt', 't'):
        search_text(dictionary)
    elif search_string in ('дата', 'по дате', 'по времени', 'date', 'время', 'time', 'timestamp', 'd'):
        search_timestamp(dictionary)
    elif search_string in ('номер', 'по номеру', 'number', 'n', 'id'):
        search_id(dictionary)
    else:
        print('Ошибка ввода. Пожалуйста, попробуйте ещё раз, используя слова "текст", "дата" или "номер".\n')


def search_id(dictionary):
    print('\nИщем по номеру')
    note_id = input('Введите номер записи: ')
    if note_id in dictionary:
        print()
        on.print_note(note_id, dictionary[note_id])
    else:
        print('\nЗаписи с таким номером нет.\n')


def search_text(dictionary):
    print('\nИщем по тексту')
    search_string = input("Введите строку для поиска: ").strip().lower()
    temp_dict = dict()
    for key, note in dictionary.items():
        for text in note:
            if search_string in text:
                temp_dict[key] = note
    if len(temp_dict) != 0:
        print('\nРезультат выборки по слову "%s" :' % search_string)
        on.print_all(temp_dict)


def search_timestamp(dictionary):
    print('\nИщем по дате')
    search_string = input(
        'Введите период для поиска в числовом формате "ГГГГ-ММ-ДД ГГГГ-ММ-ДД": ').strip()
    date = strip(search_string)
    if date == 0:
        return 0
    begin = struct_time([date[0], date[1], date[2], 0, 0, 0, 0, 0, 0])
    end = struct_time([date[3], date[4], date[5], 0, 0, 0, 0, 0, 0])
    temp_dict = dict()
    for key, note in dictionary.items():
        current = struct_time(
            [note[2][0], note[2][1], note[2][2], 0, 0, 0, 0, 0, 0])
        if current >= begin and current <= end:
            temp_dict[key] = note
    if len(temp_dict) != 0:
        print('\nРезультат выборки по дате "%s" :' % search_string)
        on.print_all(temp_dict)


def date_validation(date):
    for e in date:
        if not e.isdigit():
            return False
    if len(date[0]) != 4 or len(date[1]) > 2 or len(date[2]) > 2 or len(date[3]) != 4 or len(date[4]) > 2 or len(date[5]) > 2:
        return False
    return True


def strip(date_string):
    chars_to_remove = ['-', ',', '.', ':', 'г', 'д']
    for e in chars_to_remove:
        if e in date_string:
            date_string = date_string.replace(e, ' ')
    splitted_str_list = date_string.split()
    if not date_validation(splitted_str_list):
        print('Введены некорректные данные. Пожалуйста, повторите.',
              '\nВам необходимо ввести период, в пределах которого будет идти поиск.',
              '\nДаты должны быть введены цифрами ГГГГ-ММ-ДД ГГГГ-ММ-ДД.')
        return 0
    splitted_int_list = list()
    for e in splitted_str_list:
        splitted_int_list.append(int(e))
    return splitted_int_list
