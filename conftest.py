import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def our_browser():
    current_file = os.path.abspath(__file__) # Находим путь к текущему файлу
    project_root_dir = os.path.dirname(current_file)   #Отрезает название файла от общего пути. и оставляет общий путь до дириктории
    if not os.path.exists("tmp"): # Проверяет на наличие папки tmp в пути
        os.mkdir("tmp")
    options = webdriver.ChromeOptions()

    # Переобпределяем дефолтные пути сохранения файла
    prefs = {
        "download.default_directory": os.path.join(project_root_dir, "tmp"),
        "download.promt_for_download": False
    }

    options.add_experimental_option("prefs", prefs) # добавляются опции в общий словарь
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

