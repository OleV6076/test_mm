# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
# Создаем папку для отчетов
RUN mkdir allure-results

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Playwright и браузеры
RUN playwright install && playwright install-deps

# Копируем остальные файлы проекта
COPY . .

# Команда для запуска тестов
CMD ["pytest","--alluredir=allure-results"]

#Команда для запуска докера и копирования отчета в локальную папку
#docker run --rm -v C:\Users\user\PycharmProjects\mm\allure-results\:/app/allure-results playwright-tests