import re

from playwright.sync_api import sync_playwright, Page, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page= browser.new_page()
    page.goto("https://app.usepanda.com/#/")
    print("application succesfully launched")
    print(page.title())
    act_title = page.title
    if act_title == "Panda":
        assert True
    else:
        assert False


def test_has_title(page: Page):
            browser = p.chromium.launch(headless=False)
            page.goto("https://playwright.dev/")

            # Expect a title "to contain" a substring.
            expect(page).to_have_title(re.compile("Playwright"))




# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")
#
#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))
#
# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")
#
#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()
#
#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()