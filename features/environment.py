from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
import os


def browser_init(context):
    # Default browser is Chrome.
    browser = os.getenv("BROWSER", "chrome")

    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=options)
        print("Running tests in Firefox (headless mode)")
    else:
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)
        print("Running tests in Chrome (headless mode)")

    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print("\nStarted scenario:", scenario.name)
    browser_init(context)


def before_step(context, step):
    print("Started step:", step)


def after_step(context, step):
    if step.status == "failed":
        print("Step failed:", step)


def after_scenario(context, scenario):
    context.driver.quit()