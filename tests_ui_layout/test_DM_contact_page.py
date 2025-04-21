import time
from playwright.sync_api import Playwright, sync_playwright

from pom.DM_contact_page import ContactPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context()
    page = browser.new_page()
    #page.goto("https://dm-group.com.pl/contact/")
    contact_page = ContactPage(page)
    contact_page.navigate()
    contact_page.submit_form("Wit", "test@dm-group.com.pl", "Vans", "Contact please")


with sync_playwright() as playwright:
    test_submit_form(playwright)
    time.sleep(2)
