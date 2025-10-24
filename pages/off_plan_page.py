from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OffPlanPage(BasePage):
    OFF_PLAN_BUTTON = (By.CSS_SELECTOR, '[wized="newOffPlanLink"]')
    FILTER_DROPDOWN = (By.CSS_SELECTOR, '[data-test-id="search-and-filters-button"]')
    ANNOUNCED_OPTION = (By.CSS_SELECTOR, '[data-test-id="filter-badge-announced"]')
    PRODUCT_ITEMS = (By.CSS_SELECTOR, '[data-test-id^="project-card-"]')
    SALE_STATUS = (By.CSS_SELECTOR, '[data-test-id="project-card-sale-status"]')

    def open_off_plan(self):
        self.click(*self.OFF_PLAN_BUTTON)

    def filter_by_announced(self):
        self.click(*self.FILTER_DROPDOWN)
        self.click(*self.ANNOUNCED_OPTION)

    def verify_announced_results(self):
        status_elements = self.get_elements(*self.SALE_STATUS)
        assert len(status_elements) > 0, "No sale status elements found after filtering."

        visible_statuses = [el for el in status_elements if el.is_displayed()]
        print(f"Found {len(visible_statuses)} visible status elements")

        for el in visible_statuses:
            status = el.text.strip().lower()
            assert "announced" in status, f"Found non-Announced visible product: {status}"

        print("All visible projects are marked as Announced.")

    def verify_off_plan_page_opened(self):
        current_url = self.driver.current_url.lower()
        assert "find.reelly.io" in current_url or "off-plan" in current_url, \
            f"Off-plan page not opened. Current URL: {self.driver.current_url}"
        print("Off-plan page successfully opened.")