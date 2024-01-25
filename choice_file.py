from print_data import print_file

def choice_number_file(text):
    print_file()
    number = int(input(text))
    while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    return number
