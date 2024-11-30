import unittest
import os
from main import validate_postal_code, read_from_file, write_to_file

class TestPostalCodeFunctions(unittest.TestCase):

    # Тесты на корректные почтовые индексы
    def test_valid_postal_code(self):
        self.assertTrue(validate_postal_code("123456"))
        self.assertTrue(validate_postal_code("654321"))
        self.assertTrue(validate_postal_code("000000"))

    # Тесты на некорректные почтовые индексы
    def test_invalid_postal_code(self):
        self.assertFalse(validate_postal_code("12345"))    # слишком короткий
        self.assertFalse(validate_postal_code("1234567"))  # слишком длинный
        self.assertFalse(validate_postal_code("abc123"))   # содержит буквы
        self.assertFalse(validate_postal_code(" 123456 ")) # пробелы

    # Тесты для чтения почтовых индексов из файла
    def test_read_from_file(self):
        test_filename = "test_postal_codes.txt"
        test_content = "123456\n654321\nabcdef\n000000\n"
        
        # Создаем тестовый файл
        with open(test_filename, "w", encoding="utf-8") as file:
            file.write(test_content)
        
        # Проверяем чтение индексов
        result = read_from_file(test_filename)
        expected_result = ["123456", "654321", "abcdef", "000000"]
        self.assertEqual(result, expected_result)

        # Удаление файла после теста
        os.remove(test_filename)

    # Тесты для записи почтовых индексов в файл
    def test_write_to_file(self):
        test_filename = "test_output.txt"
        test_codes = ["123456", "654321", "abcdef", "000000"]
        
        # Запись индексов в файл
        write_to_file(test_filename, test_codes)
        
        # Проверка содержимого файла
        with open(test_filename, "r", encoding="utf-8") as file:
            result = file.read().splitlines()
        self.assertEqual(result, test_codes)

        # Удаление файла после теста
        os.remove(test_filename)

if __name__ == "__main__":
    unittest.main()
