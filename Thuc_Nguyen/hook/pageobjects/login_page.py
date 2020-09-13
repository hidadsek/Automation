from Thuc_Nguyen.hook.pageobjects.constants import LOGIN_PAGE
from Thuc_Nguyen.hook.pageobjects.base_page import BasePage


class LoginPage(BasePage):

    def input_email(self, value):
        locator = LOGIN_PAGE['EMAIL_TEXTBOX']
        self.input_text(locator, value)

    def input_password(self, value):
        locator = LOGIN_PAGE['PASSWORD_TEXTBOX']
        self.input_text(locator, value)

    def click_login_button(self):
        locator = LOGIN_PAGE['LOGIN_BUTTON']
        self.click_element(locator)

    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()
