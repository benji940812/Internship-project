from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.application import Application
import os


def browser_init(context):
    username = os.getenv("BROWSERSTACK_USERNAME", "")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY", "")

    options = webdriver.ChromeOptions()
    options.browser_version = "latest"
    options.platform_name = "Windows 10"

    bstack_options = {
        "os": "Windows",
        "osVersion": "10",
        "projectName": "Soft.reelly Off-plan Filter",
        "buildName": "BrowserStack Internship Build - Windows 10",
        "sessionName": "Verify Off-plan filtering on Reelly",
        "debug": "true",
        "networkLogs": "true",
        "consoleLogs": "info",
        "local": "false"
    }
    options.set_capability("bstack:options", bstack_options)

    context.driver = webdriver.Remote(
        command_executor=f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    print("✅ Running tests on BrowserStack (Live Mode Enabled)")


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
