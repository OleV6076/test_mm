from playwright.sync_api import expect
from pages_web.mm_ru.main_page import MainPage
import allure

@allure.feature("Поиск")
@allure.story("Проверка работы строки поиска")
def test_search_string(page):
    main_page = MainPage(page)

    with allure.step("Переход на сайт"):
        main_page.navigate()

    with allure.step("Выполнение поиска"):
        main_page.search("Мотор для лодки")

    with allure.step("Проверка отображения результатов поиска"):
        expect(page.locator("#category-content"),
               'Результаты запроса не отобразились на странице').to_be_visible()