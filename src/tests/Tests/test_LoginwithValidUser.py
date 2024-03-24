import time

from playwright.sync_api import Page, expect, sync_playwright


def test_login_with_valid_user(page: Page) -> None:
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Username / Email").click()
    page.get_by_placeholder("Username / Email").fill("preethi")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Login").click()
    time.sleep(10)
    expect(page.get_by_role("link", name=" Account")).to_be_visible()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    test_login_with_valid_user(page)
    browser.close()

