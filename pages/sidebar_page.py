from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class SidebarPage(BasePage):
    OFF_PLAN_BTN = (By.CSS_SELECTOR, "div[class*='div-block-121']")
    OFF_PLAN_TXT = (By.CSS_SELECTOR, "button[class*='pb-5']")

    def open_off_plan(self):
        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located(self.OFF_PLAN_BTN))
        self.click(*self.OFF_PLAN_BTN)

        self.wait.until(EC.visibility_of_element_located(self.OFF_PLAN_TXT))
