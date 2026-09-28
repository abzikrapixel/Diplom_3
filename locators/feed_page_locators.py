from selenium.webdriver.common.by import By

ORDERS_LIST = (By.XPATH, "//h1[text()='Лента заказов']")
ALL_TIME_ORDERS_FINISHED = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
TODAY_ORDERS_FINISHED = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul")