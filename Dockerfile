FROM mcr.microsoft.com/playwright:focal


# Устанавливаем зависимости для добавления PPA и установки Python 3.12
RUN apt-get update && apt-get install -y \
    software-properties-common \
    xvfb \
    wget \
    unzip \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update && apt-get install -y \
    python3.12 \
    python3.12-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем переменную окружения JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Устанавливаем зависимости Python
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Устанавливаем браузеры
RUN npx playwright install

# Устанавливаем Allure CLI
RUN wget -q -O /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/2.32.2/allure-2.32.2.zip && \
    unzip /tmp/allure.zip -d /opt/ && \
    ln -s /opt/allure-2.32.2/bin/allure /usr/local/bin/allure && \
    rm /tmp/allure.zip

# Копируем проект
COPY . /app
WORKDIR /app

# Команда для запуска тестов и генерации отчета Allure
CMD ["sh", "-c", "pytest --alluredir=allure-results && allure generate allure-results -o allure-report --clean"]