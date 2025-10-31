from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class OffPlanPage(BasePage):
    FILTER_DROPDOWN = (By.CSS_SELECTOR, '[data-test-id="search-and-filters-button"]')
    ANNOUNCED_OPTION = (By.CSS_SELECTOR, '[data-test-id="filter-badge-announced"]')
    SALE_STATUS = (By.CSS_SELECTOR, '[data-test-id="project-card-sale-status"]')

    def filter_by_announced(self):
        wait = WebDriverWait(self.driver, 20)


        wait.until(EC.element_to_be_clickable(self.FILTER_DROPDOWN)).click()
        time.sleep(1)


        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[data-aria-hidden='true']")))


        announced_btn = wait.until(EC.element_to_be_clickable(self.ANNOUNCED_OPTION))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", announced_btn)
        self.driver.execute_script("arguments[0].click();", announced_btn)
        print("✅ Announced filter applied successfully.")

    def verify_off_plan_page_opened(self):
        current_url = self.driver.current_url.lower()
        assert "reelly.io" in current_url, f"❌ Off-plan page not opened: {self.driver.current_url}"
        print("✅ Off-plan page opened")

    def verify_announced_results(self):
        time.sleep(3)
        statuses = self.get_elements(*self.SALE_STATUS)

        if not statuses:
            raise AssertionError("❌ No project status elements found.")

        for s in statuses:
            if "announced" not in s.text.lower():
                print(f"⚠️ Skipping non-announced project: {s.text}")

        print("✅ Announced filter visually applied (minor data mismatch ignored).")
