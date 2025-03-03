# Проект по автоматизации тестирования сайта <a target="_blank" href="https://mm.ru/"> mm.ru</a>
![Screenshot_54](https://github.com/user-attachments/assets/414f0530-61a4-404c-bc37-26c840f14fdd)

----
### Проект реализован с использованием:
<img src="design/icons/python.png" width="50">  <img src="design/icons/pysharm.png" width="50">  <img src="design/icons/pytest.png" width="50">  <img src="design/icons/playwright.png" width="50"><img src="design/icons/request.png" width="50">  <img src="design/icons/allure_report.png" width="50">  <img src="design/icons/Github.png" width="50">  <img src="design/icons/tg.png" width="50">  <img src="design/icons/docker.png" width="50"> 

----

 ### Список проверок, реализованных в web/UI автотестах

- [x] Добавление товара в Корзину
- [x] Удаление товара из Корзины
- [x] Добавление товара в Избранное
- [x] Удаление товара из Избранного
- [x] Открывается по-ап авторизации
- [x] Негативная проверка попытки входа с невалидными данными
- [x] Проверка отображения разделов каталога
- [x] Удаление товара из избранного
- [x] Проверка выполнения поиска

----
 
 ### Список проверок, реализованных в API автотестах

- [x] Запрос на получение списка пользователе
- [x] Запрос на получение создание пользователя
- [x] Запрос на обновление данных пользователя
- [x] Запрос на удаление пользователя
  
----
 
### Локальный запуск
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
mkdir my_project
cd my_project
python -m venv .venv
source .venv/bin/activate  # На Windows: .venv\Scripts\activate
pip install poetry
poetry init  # Создаст файл pyproject.toml
poetry add requests  # Добавляет requests в dependencies
poetry add --dev pytest  # Добавляет pytest в dev-dependencies
poetry install --no-root
pytest .
