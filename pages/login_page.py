import allure

from locators.login_page_locators import (
    LOGIN_EMAIL_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
)
from pages.base_page import BasePage
from helpers.urls import LOGIN_PAGE
from locators.main_page_locators import ORDER_BUTTON


class LoginPage(BasePage):

    @allure.step("Ввод email")
    def set_email(self, email):
        self.set_value(LOGIN_EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def set_password(self, password):
        self.set_value(PASSWORD_INPUT, password)

    @allure.step("Нажатие кнопки «Войти»")
    def click_login(self):
        self.click(LOGIN_BUTTON)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.open(LOGIN_PAGE)
        self.close_modal()
        self.set_email(email)
        self.set_password(password)
        self.click_login()
        self.wait_loading_gone()
        self.wait_visible(ORDER_BUTTON)