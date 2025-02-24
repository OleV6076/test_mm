import random
from pages.mm_ru.main_page import MainPage
from playwright.sync_api import  expect
from constants import  FAVORITES_URL

def test_add_to_favorite(page):

    main_page = MainPage(page)

    # Переходим на сайт
    main_page.navigate()

    # Получаем список имен товара
    product_names = main_page.get_product_names()

    # Выбираем рандомное имя
    random_product = random.choice(product_names)

    #Добавление товара в избранное
    page.get_by_role("button",name= main_page.add_name_for_the_favorites_click(random_product),exact=True).click()

    #Переходим в избранное
    main_page.navigate(FAVORITES_URL)

    # Проверяем товар с выбранным названием добавился в избранное
    expect(page.locator("[data-test-id=\"text__product-name\"]"), "Товар не добавлен в избранное").to_contain_text(
        f"{random_product}")

    # Удаление товара из избранного
    page.get_by_role("button",name= main_page.delet_name_for_the_favorites_click(random_product) ,exact=True).click()

    #После удаления товара в Избранном пусто
    expect(page.locator("[data-test-id=\"text__empty-favorite-title\"]"),"Товар не удалился из избранного"
           ).to_contain_text("Добавьте то, что понравилось")

