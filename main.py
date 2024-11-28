import re

# Проверка почтового индекса
def validate_postal_code(code):
    pattern = r"^\d{6}$"
    return re.match(pattern, code) is not None

# Ввод индексов от пользователя
def get_user_input():
    print("Введите почтовые индексы (вводите по одному индексу, для завершения введите 'стоп'):")
    user_codes = []
    while True:
        code = input("Введите индекс: ")
        if code.lower() == "стоп":
            break
        user_codes.append(code)
    return user_codes

# Чтение почтовых индексов из файла
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return []

# Запись почтовых индексов в файл
def write_to_file(file_path, codes):
    with open(file_path, 'w') as file:
        for code in codes:
            file.write(f"{code}\n")
    print(f"Индексы успешно записаны в файл '{file_path}'.")

# Проверка и вывод результатов
def check_and_display_codes(codes):
    print("\nРезультаты проверки почтовых индексов:")
    for code in codes:
        result = "корректный" if validate_postal_code(code) else "некорректный"
        print(f"'{code}': {result}")

# Мейник
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Ввести индексы вручную")
        print("2. Прочитать индексы из файла")
        print("3. Записать индексы в файл")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            user_codes = get_user_input()
            check_and_display_codes(user_codes)
        elif choice == "2":
            file_path = input("Введите путь к файлу: ")
            file_codes = read_from_file(file_path)
            check_and_display_codes(file_codes)
        elif choice == "3":
            codes_to_save = get_user_input()
            file_path = input("Введите путь для сохранения файла: ")
            write_to_file(file_path, codes_to_save)
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()