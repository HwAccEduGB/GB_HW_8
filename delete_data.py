from get_row import input_row

def delete_row():
    text_menu_change_file = "Выберите файл, в котором Вы хотите удалить строку\nВведите цифру 1 или 2: "
    number_row, data, nf = input_row(text_menu_change_file)
    del data[number_row - 1]
    data = [f'{i + 1};{data[i].split(";")[1]};'
            f'{data[i].split(";")[2]};'
            f'{data[i].split(";")[3]};'
            f'{data[i].split(";")[4]}'
            for i in range(len(data))]
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Строка успешно удалена!\n")


    