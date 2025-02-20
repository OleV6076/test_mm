from playwright.sync_api import Page
from constants import BASE_URL

class MainPage():

    def __init__(self, page: Page):
        self.page = page



    def navigate(self,url = BASE_URL):
        #Переход на главную страницу.
        self.page.goto(url, wait_until="domcontentloaded")

    def open_login(self):
        self.page.locator("[data-test-id=\"button__auth\"]").get_by_text("Войти").click()

    def search(self, query: str):
        #Выполнение поиска по запросу
        self.page.click('input[data-test-id="input__search"]')
        self.page.fill('input[data-test-id="input__search"]', query)
        self.page.locator('[data-test-id="input__search"]').press("Enter")

    def get_first_product_name(self) -> str:
        #Метод для получения текста первого продукта на странице."""
        return self.page.locator('[data-test-id="text__product-name"]').first.inner_text()

    def add_name_for_the_favorites_click(self,name) -> str:
        #Метод для формирования текста 'Добавить {имя продукта} в избранное'
        return f"Добавить {name} в избранное"

    def delet_name_for_the_favorites_click(self,name):
        #Метод для формирования текста 'Убрать {имя продукта} из избранного'
        return f"Убрать {name} из избранного"

    def get_product_names(self):
        #Ожидание появления хотя бы одного элемента с указанным локатором
        self.page.wait_for_selector('//*[@class="subtitle-item"][@data-test-id="text__product-name"]')

        #Локатор для поиска всех элементов с указанным селектором
        product_locator = self.page.locator('//*[@class="subtitle-item"][@data-test-id="text__product-name"]')

        #Получаем текстовое содержимое всех найденных элементов
        product_names = product_locator.evaluate_all("(elements) => elements.map(el => el.textContent.trim())")
        return product_names

