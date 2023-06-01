import locale
import user_interface as ui
import filehandling as fh


def main():
    locale.setlocale(locale.LC_ALL, '')
    # notes_db = {
    #     1: ["Первая заметка", "It's alive!", [2021, 5, 30, 19, 5, 18, 2, 151, 0]],
    #     2: ['Важная новость', 'Эта звезда смерти полностью функциональна и способна разрушить весь флот повстанцев одним ударом.', [2023, 4, 13, 10, 1, 52, 2, 151, 0]],
    #     3: ['Продолжаем тестировать. Немного китайщины', "大跃进", [2023, 1, 2, 10, 56, 34, 2, 151, 0]]
    # }
    choice_code = 1
    while (choice_code != 0):
        notes_db = fh.read_notes()
        choice_code = ui.user_choice(notes_db)
    fh.store_notes(notes_db)


if __name__ == "__main__":
    main()
