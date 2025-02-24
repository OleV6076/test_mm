import random
from pages.main_page import MainPage
from playwright.sync_api import expect


def test_catalog_section(page):

    main_page = MainPage(page)
    # Получаем рандомное имя раздела каталога
    section_random_name = random.choice(list(main_page.catalog_dict.keys()))
    # Получаем значение для сравнения с названием страницы
    expected_directory_name= main_page.catalog_dict.get(section_random_name)

    # Переходим на сайт
    main_page.navigate()

    # Нажать кнопку каталога
    main_page.catalog_button()

    # Проверяем что разделы каталога отобразились
    expect(page.locator("[data-test-id=\"modal__catalog\"]").get_by_text(
        "Покупки для юрлиц Электроника Бытовая техника Строительство и ремонт Дача, сад и")).to_be_visible()



    # Перейти на страницу каталога
    main_page.catalog_section(section_random_name)

    # Получаем название отображаемого раздела  каталога
    title_text = main_page.title_text()

    # Проверяем, что ожидаемое и отображаемое названия совпали
    assert  expected_directory_name == title_text, \
        f'Ожидаемое название не совпадает с отображаемым.Ожидали {expected_directory_name}, отобразилось {title_text}'