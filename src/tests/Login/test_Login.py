from playwright.sync_api import Page, expect




def test_login_with_valid_user(page: Page) -> None:
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Username / Email").click()
    page.get_by_placeholder("Username / Email").fill("preethi")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("panda-user-dropdown")).to_contain_text("preethi")


def test_login_with_invalid_user(page: Page) -> None:
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Username / Email").click()
    page.get_by_placeholder("Username / Email").fill("invaliduser")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Login").click()
    # expect(page.get_by_text("Login failed.")).to_be_visible()
   # expect(page.locator("//span[contains(text(),'Login failed.')]")).to_contain_text("Login failed.")