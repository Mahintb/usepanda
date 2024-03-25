import time

from playwright.sync_api import Page, expect, sync_playwright

def test_login_with_invalid_user(page: Page) -> None:
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Username / Email").click()
    page.get_by_placeholder("Username / Email").fill("invaliduser")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Login").click()
    time.sleep(10)
    page.wait_for_selector("//span[@ng-if='user.$invalid']",timeout=50000)
    failbutton = page.query_selector("//span[@ng-if='user.$invalid']").text_content()
    assert failbutton == "Login failed.", False




with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        test_login_with_invalid_user(page)
        browser.close()
