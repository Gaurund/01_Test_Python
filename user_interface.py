from time import gmtime
import file_handling as fh
import output_notes as on


def add_note(dictionary):
    title = input("\nВведите заголовок: ")
    text = input("Введите тело заметки: ")
    timestamp = gmtime()
    index = highest_key(dictionary)
    dictionary[str(index + 1)] = [title, text, timestamp]
    fh.store_notes(dictionary)
    print('\nЗаметка сохранена.\n')
    return dictionary


def highest_key(dictionary):
    temp_list = list(dictionary)
    temp_list.sort()
    highest_key = int(temp_list[len(temp_list)-1])
    return highest_key


def delete_note(dictionary):
    print('\nУдаление записи является необратимой операцией!')
    note_id = input(
        'Если вы уверены, что хотите удалить заметку, введите её номер: ')
    if note_id not in dictionary:
        print('\nЗаписи с таким номер нет!\n')
    else:
        confirmation = input(
            'Последний шанс передумать. \nВведите "да", если действительно хотите удалить заметку: ').strip().lower()
        if confirmation in ['да', 'д', 'yes', 'y']:
            del dictionary[note_id]
            print('\nЗаметка удалена.')
            fh.store_notes(dictionary)
    return dictionary


def edit_note(dictionary):
    note_id = input(
        '\nВведите номер заметки, которую вы хотите отредактировать: ')
    if note_id not in dictionary:
        print('\nЗаписи с таким номер нет!\n')
    else:
        print('\nТекущая запись:\n')
        on.print_note(note_id, dictionary[note_id])
        title = input("\nВведите новый заголовок: ")
        text = input("Введите новое тело заметки: ")
        timestamp = gmtime()
        dictionary[note_id] = [title, text, timestamp]
        fh.store_notes(dictionary)
        print('\nЗаметка отредактирована и сохранена.\n')
    return dictionary


def help():
    print('\nИспользуйте следующие команды:',
          '\n\t"добавить", чтобы сделать новую запись;',
          '\n\t"список", чтобы вывести все заметки одним списком;',
          '\n\t"найти", чтобы найти определённую заметку и выполнить с ней некоторое действие ',
          '\n\t"удалить", чтобы удалить определённую заметку (по номеру)',
          '\n\t"выход", чтобы покинуть приложение\n')
