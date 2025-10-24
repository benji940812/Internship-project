from behave import given, when, then
import os


@given("Open Reelly main page")
def open_main_page(context):
    context.app.login_page.open_login()

@given("Log in to Reelly account")
def login(context):
    context.app.login_page.complete_login("YOUR_EMAIL", "YOUR_PASSWORD")

@when('Click on "Off-plan" in left side menu')
def click_off_plan(context):
    context.app.sidebar_page.open_off_plan()

@then("Verify Off-plan page is opened")
def verify_off_plan_page(context):
    context.app.off_plan_page.verify_off_plan_page_opened()

@when('Filter by sale status "Announced"')
def filter_announced(context):
    context.app.off_plan_page.filter_by_announced()

@then('Verify all projects have status "Announced"')
def verify_announced(context):
    context.app.off_plan_page.verify_announced_results()
