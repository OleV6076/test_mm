from playwright.sync_api import expect

from pages.main_page import MainPage


def test_authorization(page):
    main_page = MainPage(page)

    # Переходим на сайт
    main_page.navigate()

    # Открываем поп-ап авторизации
    main_page.open_login()

    # Поверка отображения поп-апа авторизации
    expect(page.locator(".content-wrapper > div > .content"),"Поп-ап авторизации не отобразился").to_be_visible()

    # Переходим на вход по логину и паролю
    page.get_by_text("Войти по паролю").click()

    page.locator("[data-test-id=\"input__login\"]").click()
    page.locator("[data-test-id=\"input__login\"]").fill("bad@mail.ru")
    page.locator("[data-test-id=\"input__password\"]").click()
    page.locator("[data-test-id=\"input__password\"]").fill("123456789")
    page.get_by_role("button", name="Войти").click()

    # Находим элемент с ошибкой
    error_element = page.locator('.input-form-group > div.has-error')

    # Используем evaluate для получения содержимого ::after
    after_content = error_element.evaluate('element => {const afterStyles = window.getComputedStyle(element, "::after");return afterStyles.content;}')

    # Проверяем, что содержимое ::after соответствует ожидаемому тексту
    assert after_content == '"Неверный логин или пароль"', f"Ожидалось 'Неверный логин или пароль', получено {after_content}"

    page.pause()

