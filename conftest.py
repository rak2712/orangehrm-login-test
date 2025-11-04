import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
