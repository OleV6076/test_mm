# Проект по автоматизации тестирования сайта <a target="_blank" href="https://mm.ru/"> mm.ru</a>
![Screenshot_54](https://github.com/user-attachments/assets/414f0530-61a4-404c-bc37-26c840f14fdd)

----
### Проект реализован с использованием:
<img src="design/icons/python.png" width="50">  <img src="design/icons/pysharm.png" width="50">  <img src="design/icons/pytest.png" width="50">  <img src="design/icons/playwright.png" width="50"><img src="design/icons/request.png" width="50">  <img src="design/icons/allure_report.png" width="50">  <img src="design/icons/Github.png" width="50">  <img src="design/icons/tg.png" width="50">  <img src="design/icons/docker.png" width="50"> <img src="design/icons/jenkins.png" width="50">

----

#### Видео прохождения теста
> Добавлена пауза между шагами 2с для наглядности. Тест проходит по сценарию:
> Выбор рандомного товара-Переход в карточку товара-Добавление товара в Корзину-Проверка товара в корзине-Удаление товара из корзины

![686934ed8c1a2ffd689469835e26f016](https://github.com/user-attachments/assets/10d18953-bb79-42f6-8a0a-799fc1f5c342)

---

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
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
playwright install
pytest --alluredir=allure-results test/
allure serve allure-results
```

---

### Собираем image в Docker 
```
docker build -t playwright-tests .
```
![Собираем билд в докере](https://github.com/user-attachments/assets/1b203c28-d0cd-4936-847a-0ec13d23b37e)

### Запускаем контейнер с тестами дублируя Allure отчет в локальную папку из контейнера
```
 docker run --rm -v C:\Users\user\PycharmProjects\mm\allure-report\:\allure-results playwright-tests
```
![Запуск](https://github.com/user-attachments/assets/dfbc00b1-4232-4f21-a93f-5cabec764b4d)

### Allure отчет

#### Общие результаты
![Allure общий](https://github.com/user-attachments/assets/e7aeacd8-696a-423e-8411-b1df8f8ab51c)

#### Список тест кейсов в Allure 
![Allure кейсыpng](https://github.com/user-attachments/assets/4f041b03-71ce-4ac2-9de5-abd02c9b9cff)

----

#### Запуск тестов в Jenkins
>Локально развернул Jenkins в Docker с реализацией Allure отчета внутри

![Jenkins+Allure](https://github.com/user-attachments/assets/b8403c85-411e-4c58-b974-dcdab6881659)
![Jenkins+Allure 2](https://github.com/user-attachments/assets/f7337213-ff3f-472f-8586-30001dff8042)

----

>Реализована отправка результатов тестового прогона в Telegram
>Пример отчета

![image](https://github.com/user-attachments/assets/0552f06e-6fe7-4855-813d-ff0384a7e9f8)









