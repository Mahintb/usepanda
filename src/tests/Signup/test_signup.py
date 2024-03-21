from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Sign Up").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("mahin")
    page.get_by_placeholder("E-mail").click()
    page.get_by_placeholder("E-mail").fill("mahinideen@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Register").click()
    expect(page.get_by_role("button")).to_contain_text("Success")
