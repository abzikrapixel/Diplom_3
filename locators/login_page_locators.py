from selenium.webdriver.common.by import By


NAME_INPUT = (By.NAME, "name")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.XPATH,"//input[@type='password']")

LOGIN_EMAIL_INPUT = (By.XPATH,"//input[@type='text' or @type='email']")

LOGIN_BUTTON = (By.XPATH,"//button[text()='Войти']")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
