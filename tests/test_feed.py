import allure

from helpers.api import register_user
from helpers.data import PASSWORD
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.epic("UI Stellar Burgers")
@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Проверка: после заказа растёт счётчик за всё время")
    def test_all_time_orders(self, driver_with_user):
        feed_page = FeedPage(driver_with_user)
        main_page = MainPage(driver_with_user)
        login_page = LoginPage(driver_with_user)

        with allure.step("Смотрим счётчик заказа за всё время"):
            feed_page.open_orders_list()
            before = feed_page.get_all_time_orders()

        with allure.step("Входим и делаем заказ"):
            email, token = register_user()
            driver_with_user.access_token = token
            login_page.login(email, PASSWORD)
            main_page.make_order()

        with allure.step("Проверяем, что счётчик вырос"):
            feed_page.open_orders_list()
            feed_page.wait_all_time_counter_grows(before)
            assert feed_page.get_all_time_orders() > before

    @allure.title("Проверка: после заказа растёт счётчик за сегодня")
    def test_today_orders(self, driver_with_user):
        feed_page = FeedPage(driver_with_user)
        main_page = MainPage(driver_with_user)
        login_page = LoginPage(driver_with_user)

        with allure.step("Смотрим счётчик за сегодня"):
            feed_page.open_orders_list()
            before = feed_page.get_today_orders()

        with allure.step("Входим и делаем заказ"):
            email, token = register_user()
            driver_with_user.access_token = token
            login_page.login(email, PASSWORD)
            main_page.make_order()

        with allure.step("Проверяем, что счётчик вырос"):
            feed_page.open_orders_list()
            feed_page.wait_today_counter_grows(before)
            assert feed_page.get_today_orders() > before

    @allure.title("Проверка: номер заказа появляется в разделе «В работе»")
    def test_order_in_progress(self, driver_with_user):
        feed_page = FeedPage(driver_with_user)
        main_page = MainPage(driver_with_user)
        login_page = LoginPage(driver_with_user)

        with allure.step("Входим и делаем заказ"):
            email, token = register_user()
            driver_with_user.access_token = token
            login_page.login(email, PASSWORD)
            number = main_page.make_order()

        with allure.step("Открываем ленту и проверяем раздел «В работе»"):
            feed_page.open_orders_list()
            feed_page.wait_number_in_progress(number)
            assert feed_page.in_progress_has_number(number)
