from playwright.sync_api import Page, expect, sync_playwright


def test_logout(page: Page) -> None:
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Username / Email").click()
    page.get_by_placeholder("Username / Email").fill("preethi")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Login").click()
    page.goto("https://app.usepanda.com/#/")
    page.get_by_text("preethi").click()
    page.get_by_role("link", name=" Logout").click()
    expect(page.get_by_role("link", name="Log In")).to_be_visible()



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    test_logout(page)
    browser.close()