import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.smoke
def test_login(set_up)->None:
    page = set_up

    #page.wait_for_selector("link", name=" Login")
    page.get_by_role("link", name=" Login").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("test@test.com")
    page.get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Wachtwoord").click()
    page.get_by_role("textbox", name="Wachtwoord").fill("test123", timeout=2000)
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    #expect(page.get_by_role("link", name=" Login").click()).to_be_hidden()
    print("yay")





