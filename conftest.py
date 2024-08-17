import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function",
                autouse=True)     # scope="function" - будет открывать браузер для каждого теста отдельно
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver  # создает объект драйвера внутри тестовых классов
    yield driver
    driver.quit()
