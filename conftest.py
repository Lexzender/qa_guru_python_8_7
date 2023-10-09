import os
import pytest
from zipfile import ZipFile

#Создание архива с файлами
def file_archiving(path, Zip_File):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            Zip_File.write(file_path, arcname=file)


@pytest.fixture(scope="function")
def dell_zip():
    if not os.path.exists("tmp"):
        os.mkdir("tmp")

    yield

    if os.path.exists("tmp/Python.zip"):
        os.remove("tmp/Python.zip")