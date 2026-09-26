from selenium.webdriver.common.by import By

MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")
INGRIDIENTS_WINDOW_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
LOADING = (By.CSS_SELECTOR, "[class*='Modal_modal__loading']")