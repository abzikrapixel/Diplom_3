from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait as Wait
from locators.base_page_locators import MODAL_OVERLAY, LOADING

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_visible(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=20):
        return Wait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def wait_for(self, condition, timeout=20):
        return Wait(self.driver, timeout).until(condition)

    def find_element(self, locator):
        return self.wait_visible(locator)

    def close_modal(self):
        overlays = self.driver.find_elements(*MODAL_OVERLAY)
        for overlay in overlays:
            self.execute_script("arguments[0].remove();", overlay)

    def wait_loading_gone(self, timeout=20):
        Wait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(LOADING)
        )

    def click(self, locator):
        self.close_modal()
        self.wait_loading_gone()
        self.wait_clickable(locator).click()

    def send_keys(self, locator, text):
        self.set_value(locator, text)

    def set_value(self, locator, text):
        self.close_modal()
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def get_url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)