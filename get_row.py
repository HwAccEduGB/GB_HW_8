from return_data_file import data_file

def input_row(text):
    data, nf = data_file(text)
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
        # нужно придумать как вернуться в основное меню если файл пустой
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
    return number_row, data, nf

    