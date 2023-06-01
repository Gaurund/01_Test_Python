from time import strftime, struct_time


def print_all(dictionary):
    print()
    for key, note in dictionary.items():
        print_note(key, note)
    print()


def print_note(key, note):
    print("Номер записи: %s" % key)
    print("Заголовок: %s" % note[0])
    print("Заметка: %s" % note[1])
    print("Дата создания записи: %s" % strftime(
        "%H:%M:%S %d %B %Y", struct_time(note[2])))
    print('-'*16, '='*3, '<>', '='*3, '-'*16, sep='')
