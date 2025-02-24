import random
from pages_web.mm_ru.main_page import MainPage
from playwright.sync_api import expect
from constants import FAVORITES_URL
import allure


@allure.feature("Избранное")
@allure.story("Добавление товара в избранное")
def test_add_to_favorite(page):
    main_page = MainPage(page)

    with allure.step("Переход на сайт"):
        main_page.navigate()

    with allure.step("Получение списка товаров"):
        product_names = main_page.get_product_names()

    with allure.step("Выбор случайного товара"):
        random_product = random.choice(product_names)

    with allure.step(f"Добавление товара '{random_product}' в избранное"):
        page.get_by_role("button", name=main_page.add_name_for_the_favorites_click(random_product), exact=True).click()

    with allure.step("Переход в избранное"):
        main_page.navigate(FAVORITES_URL)

    with allure.step("Проверка presence товара в избранном"):
        expect(page.locator("[data-test-id=\"text__product-name\"]"),
               "Товар не добавлен в избранное").to_contain_text(f"{random_product}")

    with allure.step("Удаление товара из избранного"):
        page.get_by_role("button", name=main_page.delet_name_for_the_favorites_click(random_product),
                         exact=True).click()

    with allure.step("Проверка пустого избранного"):
        expect(page.locator("[data-test-id=\"text__empty-favorite-title\"]"),
               "Товар не удалился из избранного").to_contain_text("Добавьте то, что понравилось")