from playwright.sync_api import expect
from pages.mm_ru.main_page import MainPage


def test_search_string(page):

    main_page = MainPage(page)

    # Переходим на сайт
    main_page.navigate()

    # Выполняем поиск
    main_page.search("Мотор для лодки")

    # Проверяем, что результаты поиска отображаются
    expect(page.locator("#category-content"), 'Результаты запроса не отобразились на странице').to_be_visible()


