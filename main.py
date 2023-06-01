import locale
import user_interface as ui
import file_handling as fh


def main():
    locale.setlocale(locale.LC_ALL, '')

    choice_code = 1
    while (choice_code != 0):
        notes_db = fh.read_notes()
        choice_code = ui.user_choice(notes_db)
    fh.store_notes(notes_db)


if __name__ == "__main__":
    main()
