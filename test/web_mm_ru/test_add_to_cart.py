import random
import time

from pages_web.mm_ru.main_page import MainPage
from playwright.sync_api import expect
import allure

@allure.feature("Корзина")
@allure.story("Добавление товара в корзину")
def test_add_to_cart(page):
    main_page = MainPage(page)

    with allure.step("Переход на сайт"):
        main_page.navigate()
    time.sleep(1)

    with allure.step("Получение списка товаров"):
        product_names = main_page.get_product_names()
        assert product_names, "Список товаров пуст"
        random_product = random.choice(product_names)
    time.sleep(1)

    with allure.step(f"Добавление товара f'{random_product}' в корзину"):
        page.get_by_text(random_product).click()
        page.get_by_role("button", name="Добавить в корзину").click()
    time.sleep(1)

    with allure.step("Переход в корзину"):
        page.locator("[data-test-id=\"button__to-cart\"]").click()
    time.sleep(1)

    with allure.step("Проверка presence товара в корзине"):
        expect(page.locator("[data-test-id=\"link__product-title\"]"),
               f"Название товаров не совпадают, ожидаемый товар {random_product}").to_contain_text(f"{random_product}")
    time.sleep(1)

    with allure.step("Удаление товара из корзины"):
        page.locator("[data-test-id=\"button__delete-from-cart\"]").click()
    time.sleep(1)

    with allure.step("Проверка пустой корзины"):
        expect(page.locator("[data-test-id=\"text__empty-favorite-title\"]"),
               "Корзина не пустая, в корзине есть товар").to_contain_text("В корзине пока нет товаров")
    time.sleep(1)