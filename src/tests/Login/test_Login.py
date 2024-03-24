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
   # page.locator(".menu-icon").click()
    expect(page.get_by_text("preethi"), "preethi").to_be_visible()
  #  expect(page.get_by_role("link", name=" Account")).to_be_visible()

# expect(page.locator("panda-user-dropdown")).to_contain_text("preethi")
#  expect(page.get_by_text("Name"), "should be logged in").to_be_visible()


def test_login_with_invalid_user(page: Page) -> None:
    # hhh
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Username / Email").click()
    page.get_by_placeholder("Username / Email").fill("invaliduser")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Login").click()
    time.sleep(10)
    expect(page.get_by_text("Login failed.")).to_be_visible()


# expect(page.locator("//span[contains(text(),'Login failed.')]")).to_contain_text("Login failed.")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    test_login_with_valid_user(page)
    # page.close()
    print("mahin")
    test_login_with_invalid_user(page)
