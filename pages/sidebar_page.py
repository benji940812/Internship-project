from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class SidebarPage(BasePage):
    OFF_PLAN_BTN = (By.CSS_SELECTOR, '[wized="newOffPlanLink"]')  # 최신 locator
    OFF_PLAN_TXT = (By.CSS_SELECTOR, "button[class*='pb-5']")

    def open_off_plan(self):
        wait = WebDriverWait(self.driver, 25)


        offplan_btn = wait.until(EC.presence_of_element_located(self.OFF_PLAN_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", offplan_btn)
        time.sleep(1)


        try:
            offplan_btn.click()
            print("✅ Clicked Off-plan normally")
        except Exception:
            self.driver.execute_script("arguments[0].click();", offplan_btn)
            print("⚙️ Used JS click for Off-plan")


        wait.until(EC.visibility_of_element_located(self.OFF_PLAN_TXT))
        print("✅ Off-plan page opened successfully")
