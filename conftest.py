import os
import shutil

import pytest
from playwright.sync_api import sync_playwright

def pytest_configure():
    # Очистка папки allure-results перед запуском тестов
    allure_dir = "allure-results"
    if os.path.exists(allure_dir):
        shutil.rmtree(allure_dir)
    os.makedirs(allure_dir)

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         yield browser
#         browser.close()

# @pytest.fixture
# def page(browser):
#     context = browser.new_context(
#
#         # record_video_dir="videos/",
#         # record_video_size={"width": 1920, "height": 1080},
#         # viewport={"width": 1920, "height": 1080}
#     )
#     page = context.new_page()

    # yield page
    # context.close()