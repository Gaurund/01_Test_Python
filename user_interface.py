from time import gmtime
import searching as sc
import file_handling as fh
import output_notes as on


def add_note(dictionary):
    title = input("Введите заголовок: ")
    text = input("Введите тело заметки: ")
    timestamp = gmtime()
    index = biggest_key(dictionary)
    dictionary[index + 1] = [title, text, timestamp]
    fh.store_notes(dictionary)
    print('\nЗаметка сохранена.\n')


def biggest_key(dictionary):
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
            'Последний шанс передумать. Введите "да", если действительно хотите удалить заметку: ').strip().lower()
        if confirmation in ['да', 'д', 'yes', 'y']:
            del dictionary[note_id]
            print('\nЗаметка удалена.')
            fh.store_notes(dictionary)


def edit_note(dictionary):
    note_id = input(
        '\nВведите номер заметки, которую вы хотите отредактировать: ')
    if note_id not in dictionary:
        print('\nЗаписи с таким номер нет!\n')
    else:
        print('\nТекущая запись:\n')
        on.print_note(note_id, dictionary[note_id])
        title = input("Введите новый заголовок: ")
        text = input("Введите новое тело заметки: ")
        timestamp = gmtime()
        dictionary[note_id] = [title, text, timestamp]
        fh.store_notes(dictionary)
        print('\nЗаметка отредактирована и сохранена.\n')


def user_choice(dictionary):
    string = input(
        '\nВведите команду. Например слово "справка": ').strip().lower()
    if string in ('справка', 'помощь', 'wtf', 'help', 'h', '?'):
        help()
        return 100
    elif string in ('добавить', 'add', 'новая запись', 'a'):
        add_note(dictionary)
        return 200
    elif string in ('список', 'print all', 'все', 'all', 'p'):
        on.print_all(dictionary)
        return 300
    elif string in ('найти', 'search', 'где она', 's', 'find', 'f'):
        sc.search(dictionary)
        return 400
    elif string in ('редактировать', 'edit', 'e'):
        edit_note(dictionary)
        return 450
    elif string in ('удалить', 'delete', 'del', 'erase', 'kill', 'd'):
        delete_note(dictionary)
        return 500
    elif string in ('выход', 'выйти', 'quit', 'й', 'q', 'exit', 'авада кедавра'):
        print("\nСпасибо за внимание.")
        return 0
    print('Очень жаль, но ничего непонятно. Попробуйте ещё разок.')
    return 666


def help():
    print('\nИспользуйте следующие команды:',
          '\n\t"добавить", чтобы сделать новую запись;',
          '\n\t"список", чтобы вывести все заметки одним списком;',
          '\n\t"найти", чтобы найти определённую заметку и выполнить с ней некоторое действие ',
          '\n\t"удалить", чтобы удалить определённую заметку (по номеру)',
          '\n\t"выход", чтобы покинуть приложение\n')
