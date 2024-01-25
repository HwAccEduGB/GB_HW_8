from get_row import input_row

def copy_data():
    number_row, data, nf = input_row("Выберите файл, из которого Вы хотите копировать\nВведите цифру 1 или 2: ")
    number_file_for_write = int(input("Выберите файл, В который Вы хотите копировать\nВведите цифру 1 или 2: "))
    with open(f'db/data_{number_file_for_write}.txt', 'a', encoding='utf-8') as file:
        file.write(data[number_row-1])
    print("Данные успешно скопированы!\n")
    





