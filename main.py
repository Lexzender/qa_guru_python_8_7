import os
import time

from selene import browser, query
import requests




def test_download_file_with_selene_by_href():
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    href = browser.element("[data-testid='raw-button']").get(query.attribute("href"))  # Получаем ссылку на файл
    content = requests.get(href).content   # Получаем содержимое ссылки

    with open("pytest_readme.rst", "wb") as file:   # Записываем содержимое в файл  pytest_readme.rst
        file.write(content)

    with open("pytest_readme.rst") as file:
        text = file.read()
        assert  "framework makes it easy to write" in text   #Проверяем что файл содержит текст "framework makes
                                                                                                    # it easy to write"


def test_download_file_with_selene_by_button(our_browser):
    browser.config.driver=our_browser

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()
    time.sleep(5)

    with open ("tmp/README.rst") as file:
        text =file.read()
        assert "framework makes it easy to write" in text

