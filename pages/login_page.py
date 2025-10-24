from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[class*='login-button']")

    def open_login(self):
        self.driver.get("https://soft.reelly.io/sign-in")
        self.get_element(*self.EMAIL_FIELD)

    def login(self, email, password):
        self.type_text(*self.EMAIL_FIELD, text=email)
        self.type_text(*self.PASSWORD_FIELD, text=password)
        self.click(*self.LOGIN_BUTTON)

    def verify_home_url(self):
        self.wait.until(lambda d: "soft.reelly.io" in d.current_url)

    def complete_login(self, email, password):
        self.open_login()
        self.login(email, password)
        self.verify_home_url()
