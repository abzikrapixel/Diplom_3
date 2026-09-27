import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from helpers.api import delete_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    else:
        options = Options()
        options.set_preference("signon.autofillForms", False)
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("browser.formfill.enable", False)

        driver = webdriver.Firefox(options=options)

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def driver_with_user(driver):
    yield driver

    token = getattr(driver, "access_token", None)

    if token:
        delete_user(token)