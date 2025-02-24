from playwright.sync_api import expect

from pages.mm_ru.main_page import MainPage


def test_authorization(page):
    main_page = MainPage(page)
    username = MainPage.MAIL
    password = MainPage.PASSWORD
    invalid_mail = MainPage.INVALID_MAIL

    # Открыть  на сайт
    main_page.navigate()

    # Открываем поп-ап авторизации
    main_page.open_login()

    # Поверка отображения поп-апа авторизации
    expect(page.locator(".content-wrapper > div > .content"),"Поп-ап авторизации не отобразился").to_be_visible()

    # Вход по логину и паролю
    main_page.perform_login(username,password)

    # Находим элемент с ошибкой
    error_element = page.locator('.input-form-group > div.has-error')

    # Используем evaluate для получения содержимого ::after
    after_content = error_element.evaluate('element => {const afterStyles = window.getComputedStyle(element, "::after");return afterStyles.content;}')

    # Проверяем, что содержимое ::after соответствует ожидаемому тексту
    assert after_content == '"Неверный логин или пароль"', f"Ожидалось 'Неверный логин или пароль', получено {after_content}"



