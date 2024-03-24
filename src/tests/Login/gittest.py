import re

import playwright
from playwright.sync_api import Page, expect, sync_playwright




def test_has_title(page: Page):
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_placeholder("Username / Email").click()
    page.get_by_placeholder("Username / Email").fill("preethi")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Login").click()

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Panda"))
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=5000)
    page= browser.new_page()
    test_has_title(page)
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()