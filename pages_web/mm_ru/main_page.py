
from playwright.sync_api import Page
from constants import BASE_URL

class MainPage():

    MAIL = 'example@mail.ru'
    PASSWORD = "123456789"
    INVALID_MAIL = 'example@@mail.ru'

    # Разделы каталога и их названия после открытия
    catalog_dict = {'Электроника': 'Электроника', 'Бытовая техника': 'Бытовая техника',
                    'Строительство и ремонт': 'Товары для строительства и ремонта',
                    'Дача, сад и огород': 'Товары для дачи и сада',
                    'Одежда': 'Одежда', 'Обувь': 'Обувь', 'Аксессуары': 'Аксессуары', 'Красота': 'Товары для красоты',
                    'Бытовая химия и личная гигиена': 'Бытовая химия и средства личной гигиены',
                    'Товары для дома': 'Товары для дома',
                    'Автотовары': 'Автотовары', 'Детские товары': 'Детские товары',
                    'Хобби и творчество': 'Товары для хобби и творчества',
                    'Здоровье': 'Товары для здоровья', 'Спорт и отдых': 'Товары для спорта и отдыха',
                    'Зоотовары': 'Зоотовары',
                    'Товары для взрослых': 'Товары для взрослых', 'Продукты питания': 'Продукты питания',
                    'Канцтовары': 'Канцтовары',
                    'Книги': 'Книги', 'Автомобили': 'Автомобили'}


    def __init__(self, page: Page):
        self.page = page
        self.switch_to_password_login_button = page.get_by_text("Войти по паролю")
        self.login_input = page.locator("[data-test-id=\"input__login\"]")
        self.password_input = page.locator("[data-test-id=\"input__password\"]")
        self.login_button = page.get_by_role("button", name="Войти")


    def submit_login(self):
        # Нажимаем кнопку Войти
        self.login_button.click()

    def catalog_button(self):
        # Открыть каталог
        self.page.locator("[data-test-id=\"button__catalog\"]").click()

    def catalog_section(self, section):
        # Перейти на страницу каталога
        self.page.locator("[data-test-id=\"modal__catalog\"]").get_by_role("link", name=section).click()

    def switch_to_password_login(self):
        # Переключаем на форму ввода логина и пароля
        self.switch_to_password_login_button.click()

    def enter_credits(self,username,password):
        # Ввод логин и пароль
        self.login_input.click()
        self.login_input.fill(username)
        self.password_input.click()
        self.password_input.fill(password)

    def perform_login(self,username,password):
        # Выполнение полного процесса входа после открытия формы
        self.switch_to_password_login()
        self.enter_credits(username,password)
        self.submit_login()

    def navigate(self,url = BASE_URL):
        #Переход на главную страницу.
        self.page.goto(url, wait_until="domcontentloaded")

    def open_login(self):
        # Открыть поп-ап авторизации
        self.page.locator("[data-test-id=\"button__auth\"]").get_by_text("Войти").click()

    def search(self, query: str):
        #Выполнение поиска по запросу
        self.page.click('input[data-test-id="input__search"]')
        self.page.fill('input[data-test-id="input__search"]', query)
        self.page.locator('[data-test-id="input__search"]').press("Enter")

    def get_first_product_name(self) -> str:
        #Метод для получения текста первого продукта на странице.
        return self.page.locator('[data-test-id="text__product-name"]').first.inner_text()

    def add_name_for_the_favorites_click(self,name) -> str:
        # Метод для формирования текста 'Добавить {имя продукта} в избранное'
        return f"Добавить {name} в избранное"

    def delet_name_for_the_favorites_click(self,name):
        #Метод для формирования текста 'Убрать {имя продукта} из избранного'
        return f"Убрать {name} из избранного"

    def get_product_names(self):
        #Получение текста названия продукции на главной странице


        #Ожидание появления хотя бы одного элемента с указанным локатором
        self.page.wait_for_selector('//*[@class="subtitle-item"][@data-test-id="text__product-name"]')

        #Локатор для поиска всех элементов с указанным селектором
        product_locator = self.page.locator('//*[@class="subtitle-item"][@data-test-id="text__product-name"]')

        #Получаем текстовое содержимое всех найденных элементов
        product_names = product_locator.evaluate_all("(elements) => elements.map(el => el.textContent.trim())")
        return product_names

    def title_text(self):
        # Получаем название отображаемого раздела  каталога
        return self.page.locator("[data-test-id=\"text__title\"]").inner_text().rstrip()