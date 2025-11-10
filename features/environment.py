from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.application import Application
from dotenv import load_dotenv
import os


load_dotenv()


def browser_init(context):

    username = os.getenv("BROWSERSTACK_USERNAME", "")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY", "")


    options = webdriver.ChromeOptions()
    options.browser_version = "latest"


    bstack_options = {
        "deviceName": "iPhone 15 Pro",     #change to Samsung, Pixel, etc. if you want
        "osVersion": "17",
        "realMobile": "true",
        "projectName": "Soft.reelly Mobile Web",
        "buildName": "BrowserStack Internship Build - iPhone",
        "sessionName": "Verify Reelly Off-plan Filter on Mobile",
        "debug": "true",
        "networkLogs": "true",
        "consoleLogs": "info"
    }

    options.set_capability("bstack:options", bstack_options)

    context.driver = webdriver.Remote(
        command_executor=f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)

    print("✅ Running tests on BrowserStack (MOBILE mode - iPhone 15 Pro)")


def before_scenario(context, scenario):
    print(f"\nStarted scenario: {scenario.name}")
    browser_init(context)


def before_step(context, step):
    print(f"\nStarted step: {step.name}")


def after_step(context, step):
    if step.status == "failed":
        print(f"\nStep failed: {step.name}")


def after_scenario(context, scenario):
    context.driver.quit()
