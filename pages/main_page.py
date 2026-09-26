from locators.main_page_locators import *
from locators.base_page_locators import *
from helpers.urls import MAIN_PAGE
from pages.base_page import BasePage

class MainPage(BasePage):

    def main_title_is_visible(self):
        self.find_element(MAIN_TITLE)
        return True

    def click_constructor(self):
        self.click(CONSTRUCTOR_BUTTON)

    def click_orders_list(self):
        self.click(ORDERS_LIST_BUTTON)

    def click_ingredient(self):
        self.click(INGREDIENT)

    def ingredient_details_is_visible(self):
        self.find_element(INGRIDIENTS_DETAILS)
        return True

    def close_ingredient_details(self):
        self.click(INGRIDIENTS_WINDOW_CLOSE)

    def get_ingredient_counter(self):
        ingredient = self.find_element(INGREDIENT)
        return int(ingredient.find_element(*INGREDIENT_COUNTER).text)

    def add_ingredient_to_order(self):
        source = self.find_element(INGREDIENT)
        target = self.find_element(CONSTRUCTOR_BASKET)
        self.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const data = new DataTransfer();
            data.setData('text/plain', source.href || 'ingredient');
            const event = { bubbles: true, cancelable: true, dataTransfer: data };
            source.dispatchEvent(new DragEvent('dragstart', event));
            target.dispatchEvent(new DragEvent('dragenter', event));
            target.dispatchEvent(new DragEvent('dragover', event));
            target.dispatchEvent(new DragEvent('drop', event));
            source.dispatchEvent(new DragEvent('dragend', event));
            """,
            source,
            target,
        )

    def click_enter_account(self):
        self.click(ENTER_ACCOUNT_BUTTON)

    def click_order(self):
        self.click(ORDER_BUTTON)

    def get_order_number(self):
        self.wait_visible(ORDER_NUMBER, 30)
        self.wait_for(
            lambda _driver: self.get_text(ORDER_NUMBER) not in ("", "9999"),
            30,
        )
        return self.get_text(ORDER_NUMBER)

    def make_order(self):
        self.wait_loading_gone()
        self.wait_visible(ORDER_BUTTON, 30)
        self.main_title_is_visible()
        self.add_ingredient_to_order()
        self.wait_clickable(ORDER_BUTTON, 30).click()
        return self.get_order_number()

    def open_constructor(self):  # изменение
        self.open(MAIN_PAGE)