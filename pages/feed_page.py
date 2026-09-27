import allure

from helpers.urls import FEED_PAGE
from locators.feed_page_locators import (
    ORDERS_LIST,
    ALL_TIME_ORDERS_FINISHED,
    TODAY_ORDERS_FINISHED,
    IN_PROGRESS,
)

from pages.base_page import BasePage


class FeedPage(BasePage):
    
    def orders_list_is_visible(self):
        return bool(self.find_element(ORDERS_LIST))    

    @allure.step("Открытие ленты заказов")
    def open_orders_list(self):
        self.open(FEED_PAGE)
        self.wait_visible(ORDERS_LIST)


    @allure.step("Получение счётчика «Выполнено за всё время»")
    def get_all_time_orders(self):
        return int(self.get_text(ALL_TIME_ORDERS_FINISHED))

    @allure.step("Получение счётчика «Выполнено за сегодня»")
    def get_today_orders(self):
        return int(self.get_text(TODAY_ORDERS_FINISHED))

    @allure.step("Проверка наличия заказа в разделе «В работе»")
    def in_progress_has_number(self, number):
        text = self.get_text(IN_PROGRESS)

        full_number = str(number).zfill(7)
        short_number = str(number).lstrip("0")

        return (
            full_number in text
            or short_number in text
            or str(number) in text
        )

    @allure.step("Ожидание увеличения счётчика за всё время")
    def wait_all_time_counter_grows(self, before):
        self.wait_for(
            lambda driver: self.get_all_time_orders() > before
        )

    @allure.step("Ожидание увеличения счётчика за сегодня")
    def wait_today_counter_grows(self, before):
        self.wait_for(
            lambda driver: self.get_today_orders() > before
        )

    @allure.step("Ожидание появления заказа в разделе «В работе»")
    def wait_number_in_progress(self, number):
        def order_is_visible(driver):
            if self.in_progress_has_number(number):
                return True

            self.open_orders_list()
            return self.in_progress_has_number(number)

        self.wait_for(order_is_visible, 30)
