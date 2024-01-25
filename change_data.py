from get_row import input_row

def change_data():
    number_row, data, nf = input_row("Выберите файл, в который хотите внести изменения\nВведите цифру 1 или 2: ")
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    birthdate = input("Введите дату рождения: ")
    town = input("Введите город: ")
    data[number_row - 1] = f'{number_row};{name};{surname};{birthdate};{town}\n'
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!\n")
