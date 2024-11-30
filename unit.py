import unittest
import os
from main import validate_postal_code, read_from_file, write_to_file, check_and_display_codes

class TestPostalCodeFunctions(unittest.TestCase):
    # Тесты для проверки корректности почтовых индексов
    def test_valid_postal_code(self):
        self.assertTrue(validate_postal_code("123456"))
        self.assertTrue(validate_postal_code("654321"))
        self.assertTrue(validate_postal_code("000000"))
        
    def test_invalid_postal_code(self):
        self.assertFalse(validate_postal_code("12345"))  # Слишком короткий
        self.assertFalse(validate_postal_code("1234567"))  # Слишком длинный
        self.assertFalse(validate_postal_code("abc123"))  # С буквами
        self.assertFalse(validate_postal_code("12 3456"))  # С пробелами

    # Тесты для чтения почтовых индексов из файла
    def test_read_from_file(self):
        test_filename = "test_codes.txt"
        test_data = "123456\n654321\nabcdef\n"
        expected_result = ["123456", "654321", "abcdef"]
        
        # Записываем тестовые данные в файл
        with open(test_filename, "w", encoding="utf-8") as file:
            file.write(test_data)

        # Проверяем, что чтение из файла правильно
        self.assertEqual(read_from_file(test_filename), expected_result)

        # Удаляем тестовый файл после завершения теста
        os.remove(test_filename)

    # Тесты для записи почтовых индексов в файл
    def test_write_to_file(self):
        test_filename = "output_codes.txt"
        codes_to_write = ["123456", "654321", "000000"]

        # Записываем индексы в файл
        write_to_file(test_filename, codes_to_write)

        # Считываем и проверяем содержимое файла
        with open(test_filename, "r", encoding="utf-8") as file:
            result = file.read().splitlines()
        self.assertEqual(result, codes_to_write)

        # Удаляем тестовый файл после завершения теста
        os.remove(test_filename)

    # Тест на вывод результатов проверки индексов
    def test_check_and_display_codes(self):
        codes = ["123456", "12345", "654321", "000 000"]
        expected_output = [
            "'123456': корректный",
            "'12345': некорректный",
            "'654321': корректный",
            "'000 000': некорректный"
        ]

        output = []
        for code in codes:
            result = "корректный" if validate_postal_code(code) else "некорректный"
            output.append(f"'{code}': {result}")

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
