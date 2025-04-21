import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(page):
    #browser = playwright.chromium.launch(headless=False)
    #context = browser.new_context()
    #page = context.new_page()
    page.goto("https://indewal.nl")
    page.set_default_timeout(8000)

    yield page

@pytest.fixture
def set_up_dm(page):
    page.goto("https://dm-group.com.pl")
    page.set_default_timeout(8000)

    yield page