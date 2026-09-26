from selenium.webdriver.common.by import By

CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
ORDERS_LIST_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/')]")
INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")
CONSTRUCTOR_BASKET = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
INGRIDIENTS_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")