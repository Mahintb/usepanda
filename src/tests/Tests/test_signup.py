import time

import pytest
from playwright.sync_api import Page, expect, sync_playwright


def test_signup(page : Page) -> None:
    page.goto("https://app.usepanda.com/#/")
    page.get_by_role("link", name="Sign Up").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("fchgjghxrf")  #give random name
    page.get_by_placeholder("E-mail").click()
    page.get_by_placeholder("E-mail").fill("mahintb@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("1234567")
    page.get_by_role("button", name="Register").click()
    time.sleep(10)
    page.wait_for_selector("//button[normalize-space()='Success']",timeout=50000)
    time.sleep(10)
    successbutton = page.query_selector("//button[normalize-space()='Success']").text_content()
    assert successbutton=="Success",False

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page=browser.new_page()
    test_signup(page)


