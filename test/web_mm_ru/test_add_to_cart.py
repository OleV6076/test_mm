import random
from pages.main_page import MainPage
from playwright.sync_api import Page, expect
from constants import  FAVORITES_URL

def test_add_to_favorite(page):

    main_page = MainPage(page)

    # Переходим на сайт
    main_page.navigate()

    # Получаем список имен товара
    product_names = main_page.get_product_names()
    
    # Выбираем рандомное имя
    random_product = random.choice(product_names)

    # Переходим в карточку товара
    page.get_by_text(random_product).click()

    # товар в Корзину
    page.get_by_role("button", name="Добавить в корзину").click()

    # Переходим в CheckOut
    page.locator("[data-test-id=\"button__to-cart\"]").click()

    # Проверяем, что товар с таким же названием отображается в корзине
    expect(page.locator("[data-test-id=\"link__product-title\"]"),
           f"Название товаров не совпадают, ожидаемый товар {random_product}").to_contain_text(f"{random_product}")

    # Удаляем товар из корзины
    page.locator("[data-test-id=\"button__delete-from-cart\"]").click()

    # Проверяем, что корзина пустая
    expect(page.locator("[data-test-id=\"text__empty-favorite-title\"]"),
           "Корзина не пустая, в корзине есть товар").to_contain_text("В корзине пока нет товаров")




