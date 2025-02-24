from playwright.sync_api import expect
from pages_web.mm_ru.main_page import MainPage
import allure

@allure.feature("Авторизация")
@allure.story("Попытка входа с неверными учетными данными")
def test_authorization(page):
    main_page = MainPage(page)
    username = MainPage.MAIL
    password = MainPage.PASSWORD
    invalid_mail = MainPage.INVALID_MAIL

    with allure.step("Переход на сайт"):
        main_page.navigate()

    with allure.step("Открытие поп-апа авторизации"):
        main_page.open_login()

    with allure.step("Проверка отображения поп-апа авторизации"):
        expect(page.locator(".content-wrapper > div > .content"),
               "Поп-ап авторизации не отобразился").to_be_visible()

    with allure.step("Попытка входа с неверными данными"):
        main_page.perform_login(username, password)

    with allure.step("Проверка сообщения об ошибке"):
        error_element = page.locator('.input-form-group > div.has-error')
        after_content = error_element.evaluate('element => {const afterStyles = window.getComputedStyle(element, "::after"); return afterStyles.content;}')
        assert after_content == '"Неверный логин или пароль"', f"Ожидалось 'Неверный логин или пароль', получено {after_content}"