import playwright
from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pom.home_page_elements import HomePage

def test_about_us_section_verbiage(set_up_dm):
    page = set_up_dm
    home_page = HomePage(page)
    expect(home_page.about_header).to_be_visible()
    expect(home_page.about_body).to_be_visible()

    #context.close()
    #browser.close()