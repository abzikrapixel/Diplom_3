from selenium.webdriver.common.by import By


PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@type='text' or @type='email']")
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
