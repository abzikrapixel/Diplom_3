from locators.login_page_locators import *
from pages.base_page import BasePage
from helpers.urls import LOGIN_PAGE
from locators.main_page_locators import ORDER_BUTTON

class LoginPage(BasePage):

    def set_email(self, email):
        self.set_value(LOGIN_EMAIL_INPUT, email)

    def set_password(self, password):
        self.set_value(PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LOGIN_BUTTON)

    def login(self, email, password):
        self.open(LOGIN_PAGE)
        self.close_modal()
        self.set_email(email)
        self.set_password(password)
        self.click_login()
        self.wait_loading_gone()
        self.wait_visible(ORDER_BUTTON)