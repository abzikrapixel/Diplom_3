import allure

from helpers.urls import MAIN_PAGE
from locators.main_page_locators import (
    CONSTRUCTOR_BUTTON,
    ORDERS_LIST_BUTTON,
    MAIN_TITLE,
    INGREDIENT,
    INGREDIENT_COUNTER,
    CONSTRUCTOR_BASKET,
    ORDER_BUTTON,
    ORDER_NUMBER,
    INGRIDIENTS_DETAILS,
)
from locators.base_page_locators import INGRIDIENTS_WINDOW_CLOSE

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Проверка отображения главной страницы")
    def main_title_is_visible(self):
        return bool(self.find_element(MAIN_TITLE))

    @allure.step("Нажатие «Конструктор»")
    def click_constructor(self):
        self.click(CONSTRUCTOR_BUTTON)

    @allure.step("Нажатие «Лента заказов»")
    def click_orders_list(self):
        self.click(ORDERS_LIST_BUTTON)

    @allure.step("Выбор ингредиента")
    def click_ingredient(self):
        self.click(INGREDIENT)

    @allure.step("Проверка отображения деталей ингредиента")
    def ingredient_details_is_visible(self):
        return bool(self.find_element(INGRIDIENTS_DETAILS))

    @allure.step("Закрытие деталей ингредиента")
    def close_ingredient_details(self):
        self.click(INGRIDIENTS_WINDOW_CLOSE)

    @allure.step("Получение счётчика ингредиента")
    def get_ingredient_counter(self):
        ingredient = self.find_element(INGREDIENT)
        return int(
            ingredient.find_element(*INGREDIENT_COUNTER).text
        )

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        source = self.find_element(INGREDIENT)
        target = self.find_element(CONSTRUCTOR_BASKET)

        self.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const data = new DataTransfer();
            data.setData('text/plain', source.href || 'ingredient');

            const event = {
                bubbles: true,
                cancelable: true,
                dataTransfer: data
            };

            source.dispatchEvent(new DragEvent('dragstart', event));
            target.dispatchEvent(new DragEvent('dragenter', event));
            target.dispatchEvent(new DragEvent('dragover', event));
            target.dispatchEvent(new DragEvent('drop', event));
            source.dispatchEvent(new DragEvent('dragend', event));
            """,
            source,
            target,
        )

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        self.wait_visible(ORDER_NUMBER, 30)

        self.wait_for(
            lambda _driver: self.get_text(ORDER_NUMBER)
            not in ("", "9999"),
            30,
        )

        return self.get_text(ORDER_NUMBER)

    @allure.step("Создание заказа")
    def make_order(self):
        self.wait_loading_gone()
        self.wait_visible(ORDER_BUTTON, 30)
        self.main_title_is_visible()

        self.add_ingredient_to_order()
        self.wait_clickable(ORDER_BUTTON, 30).click()

        return self.get_order_number()

    @allure.step("Открытие конструктора")
    def open_constructor(self):
        self.open(MAIN_PAGE)