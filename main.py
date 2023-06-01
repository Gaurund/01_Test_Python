import locale
import user_interface as ui
import file_handling as fh
import output_notes as on
import searching as sc


def main():
    locale.setlocale(locale.LC_ALL, '')

    quit_flag = True
    notes_db = fh.read_notes()
    while quit_flag:
        string = input(
            '\nВведите команду. Например слово "справка": ').strip().lower()
        if string in ('справка', 'помощь', 'wtf', 'help', 'h', '?'):
            ui.help()
        elif string in ('добавить', 'add', 'новая запись', 'a'):
            notes_db = ui.add_note(notes_db)
        elif string in ('список', 'print all', 'все', 'all', 'p'):
            on.print_all(notes_db)
        elif string in ('найти', 'search', 'где она', 's', 'find', 'f'):
            sc.search(notes_db)
        elif string in ('редактировать', 'edit', 'e'):
            notes_db = ui.edit_note(notes_db)
        elif string in ('удалить', 'delete', 'del', 'erase', 'kill', 'd'):
            notes_db = ui.delete_note(notes_db)
        elif string in ('выход', 'выйти', 'quit', 'й', 'q', 'exit', 'авада кедавра'):
            print("\nРабота завершена.")
            quit_flag = False
        else:
            print('\nОчень жаль, но ничего непонятно. Попробуйте ещё раз.')
    fh.store_notes(notes_db)


if __name__ == "__main__":
    main()
