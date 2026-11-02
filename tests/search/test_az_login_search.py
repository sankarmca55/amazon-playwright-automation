import pytest

from playwright.sync_api import sync_playwright, expect

from conftest import page
from utils.data_reader import login_data

from pages.login_page import LoginPage
from utils.config import BASE_URL

@pytest.mark.login
@pytest.mark.smoke
def test_amazon_login(page):
    valid_username = login_data["valid_login"]["username"]
    valid_password = login_data["valid_login"]["password"]

    page.goto(BASE_URL, wait_until="domcontentloaded")

    login_page = LoginPage(page)
    
    login_page.sign_other_click()

    login_page.enter_username(valid_username)
    login_page.click_continue()

    login_page.enter_password(valid_password)

    login_page.click_sign_in()
    
    #Enter text in the search box
    
    page.wait_for_timeout(2000)
    # Search box
    #search_box = page.locator("#twotabsearchtextbox")
    #search_box.fill("iphone 18 pro (1 tb) - burgundy")
    page.wait_for_timeout(2000)
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.wait_for_timeout(2000)
    page.get_by_role("searchbox", name="Search Amazon.in").fill("iphone 18 pro (1 tb) - burgundy")


    #login_page.click_sign_in()

    page.wait_for_timeout(2000)

    #login_page.nav_hover()
    #login_page.nav_signout()

@pytest.mark.search
def test_search_suggestions(page):
    page.goto("https://www.amazon.in/")

    search_box = page.locator("#twotabsearchtextbox")
    expect(search_box).to_be_visible()
    page.wait_for_timeout(2000)
    search_box.fill("iphone 18 pro (1 tb) - burgundy")
    page.wait_for_timeout(2000)
    suggestions = page.locator(
        "div.s-suggestion"
    )
    page.wait_for_timeout(2000)
    expect(suggestions.first).to_be_visible()