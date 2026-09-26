import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage

@allure.epic("UI Stellar Burgers")
@allure.feature("Основной функционал")
class TestMain:

    @allure.title("Проверка: перехода по клику на Конструктор")
    def test_constructor_button_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            feed_page = FeedPage(driver_chrome)
            main_page = MainPage(driver_chrome)
        with allure.step("Открыть ленту заказов"):
            feed_page.open_orders_list()
        with allure.step("Нажать Конструктор"):
            main_page.click_constructor()
        with allure.step("Проверить, что открыт конструктор"):
            assert main_page.main_title_is_visible()

    @allure.title("Проверка: перехода по клику на Конструктор")
    def test_constructor_button_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            feed_page = FeedPage(driver_firefox)
            main_page = MainPage(driver_firefox)
        with allure.step("Открыть ленту заказов"):
            feed_page.open_orders_list()
        with allure.step("Нажать Конструктор"):
            main_page.click_constructor()
        with allure.step("Проверить, что открыт конструктор"):
            assert main_page.main_title_is_visible()

    @allure.title("Проверка: перехода по клику на Лента заказов")
    def test_orders_list_button_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            main_page = MainPage(driver_chrome)
            feed_page = FeedPage(driver_chrome)
        with allure.step("Открыть главную"):
            main_page.open_constructor()
        with allure.step("Нажать Лента заказов"):
            main_page.click_orders_list()
        with allure.step("Проверить переход в ленту"):
            assert feed_page.orders_list_is_visible()

    @allure.title("Проверка: перехода по клику на Лента заказов")
    def test_orders_list_button_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            main_page = MainPage(driver_firefox)
        feed_page = FeedPage(driver_firefox)
        with allure.step("Открыть главную"):
            main_page.open_constructor()
        with allure.step("Нажать Лента заказов"):
            main_page.click_orders_list()
        with allure.step("Проверить переход в ленту"):
            assert feed_page.orders_list_is_visible()

    @allure.title("По клику на ингредиент открывается окно с деталями")
    def test_ingredient_details_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            main_page = MainPage(driver_chrome)
        with allure.step("Открыть главную и кликнуть ингредиент"):
            main_page.open_constructor()
            main_page.click_ingredient()
        with allure.step("Проверить окно деталей"):
            assert main_page.ingredient_details_is_visible()

    @allure.title("По клику на ингредиент открывается окно с деталями")
    def test_ingredient_details_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            main_page = MainPage(driver_firefox)
        with allure.step("Открыть главную и кликнуть ингредиент"):
            main_page.open_constructor()
            main_page.click_ingredient()
        with allure.step("Проверить окно деталей"):
            assert main_page.ingredient_details_is_visible()

    @allure.title("Окно с деталями закрывается по крестику")
    def test_ingredient_details_close_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            main_page = MainPage(driver_chrome)
        with allure.step("Открыть детали ингредиента"):
            main_page.open_constructor()
            main_page.click_ingredient()
        with allure.step("Закрыть окно крестиком"):
            main_page.close_ingredient_details()
        with allure.step("Проверить, что снова видна главная"):
            assert main_page.main_title_is_visible()

    @allure.title("Окно с деталями закрывается по крестику")
    def test_ingredient_details_close_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            main_page = MainPage(driver_firefox)
        with allure.step("Открыть детали ингредиента"):
            main_page.open_constructor()
            main_page.click_ingredient()
        with allure.step("Закрыть окно крестиком"):
            main_page.close_ingredient_details()
        with allure.step("Проверить, что снова видна главная"):
            assert main_page.main_title_is_visible()

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_orders_chrome(self, driver_chrome):
        with allure.step("Запускаем Chrome"):
            main_page = MainPage(driver_chrome)
        with allure.step("Открыть главную и запомнить счётчик"):
            main_page.open_constructor()
            before = main_page.get_ingredient_counter()
        with allure.step("Добавить ингредиент в заказ"):
            main_page.add_ingredient_to_order()
            after = main_page.get_ingredient_counter()
        with allure.step("Проверить, что счётчик вырос"):
            assert after > before

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_orders_firefox(self, driver_firefox):
        with allure.step("Запускаем Firefox"):
            main_page = MainPage(driver_firefox)
        with allure.step("Открыть главную и запомнить счётчик"):
            main_page.open_constructor()
            before = main_page.get_ingredient_counter()
        with allure.step("Добавить ингредиент в заказ"):
            main_page.add_ingredient_to_order()
            after = main_page.get_ingredient_counter()
        with allure.step("Проверить, что счётчик вырос"):
            assert after > before