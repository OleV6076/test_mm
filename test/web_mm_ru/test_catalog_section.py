import random
from pages_web.mm_ru.main_page import MainPage
from playwright.sync_api import expect
import allure

@allure.feature("Каталог")
@allure.story("Проверка разделов каталога")
def test_catalog_section(page):
    main_page = MainPage(page)

    with allure.step("Выбор случайного раздела каталога"):
        section_random_name = random.choice(list(main_page.catalog_dict.keys()))
        expected_directory_name = main_page.catalog_dict.get(section_random_name)

    with allure.step("Переход на сайт"):
        main_page.navigate()

    with allure.step("Открытие каталога"):
        main_page.catalog_button()

    with allure.step("Проверка отображения разделов каталога"):
        expect(page.locator("[data-test-id=\"modal__catalog\"]").get_by_text(
            "Покупки для юрлиц Электроника Бытовая техника Строительство и ремонт Дача, сад и")).to_be_visible()

    with allure.step(f"Переход в раздел '{section_random_name}'"):
        main_page.catalog_section(section_random_name)

    with allure.step("Проверка названия выбранного раздела"):
        title_text = main_page.title_text()
        assert expected_directory_name == title_text, \
            f'Ожидаемое название не совпадает с отображаемым. Ожидали {expected_directory_name}, отобразилось {title_text}'