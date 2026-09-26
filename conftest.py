import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from helpers.api import delete_user

@pytest.fixture
def driver_chrome():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def driver_firefox():
    options = Options()
    options.set_preference("signon.autofillForms", False)
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("browser.formfill.enable", False)
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def chrome_with_user(driver_chrome):
    yield driver_chrome
    token = getattr(driver_chrome, "access_token", None)
    if token:
        delete_user(token)

@pytest.fixture
def firefox_with_user(driver_firefox):
    yield driver_firefox
    token = getattr(driver_firefox, "access_token", None)
    if token:
        delete_user(token)