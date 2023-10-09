from zipfile import ZipFile
from conftest import file_archiving

my_file = ["file_example_XLSX_50.xlsx", "file_example_XLS_10.xls", "hello.zip",
               "Python Testing with Pytest (Brian Okken) (1).pdf", "text.txt"]

def test_file(dell_zip):
    # Создаем архив с файлами
    with ZipFile('tmp/Python.zip', 'w') as zip_File:
        file_archiving('resources/', zip_File)

    # Проверяем, что созданный архив содержит нужные документы
    with ZipFile("tmp/Python.zip") as zip_File:
        info = zip_File.infolist()
        for i in info:
            assert i.filename in my_file, f"{i.filename}: Файл не найден в архиве"

def test_count_file(dell_zip):
    # Создаем архив с файлами
    with ZipFile('tmp/Python.zip', 'w') as zip_File:
        file_archiving('resources/', zip_File)

    # Проверяем количество файлов в архиве
    with ZipFile("tmp/Python.zip") as zip_File:
        info = zip_File.namelist()
        assert len(info) == 5, f"Количество файлов в архиве != 5"