from selenium.webdriver.common.by import By

NAME_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[2]")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
LOGIN_EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[1]")