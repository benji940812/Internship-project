from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.off_plan_page import OffPlanPage
from pages.sidebar_page import SidebarPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.sidebar_page = SidebarPage(driver)