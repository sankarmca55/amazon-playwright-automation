from playwright.sync_api import sync_playwright, expect
import pytest
from utils.data_reader import login_data

from pages.login_page import LoginPage

@pytest.mark.login
def test_amazon_invalid_email(page):
 
    invalidemail = login_data["invalid_username"]["username"]
    page.goto("https://www.amazon.in/", wait_until="domcontentloaded")
        
    login_page = LoginPage(page)

    login_page.sign_other_click()
    
    login_page.enter_username(invalidemail)
    login_page.click_continue()

    page.wait_for_timeout(2000)

    # Get error message
    error_message = page.get_by_text("Invalid email address").inner_text()
    print(f"TC_LOGIN_002 Error message: {error_message}")


@pytest.mark.login
def test_amazon_invalid_mobile(page):
    invalid_mobile = login_data["invalid_mobile"]["username"]

    page.goto("https://www.amazon.in/", wait_until="domcontentloaded")

    login_page = LoginPage(page)

    login_page.sign_other_click()

    login_page.enter_username(invalid_mobile)
    login_page.click_continue()

    page.wait_for_timeout(2000)

    error_message = page.get_by_text("Invalid mobile number").inner_text()
    print(f"TC_LOGIN_003 Error message: {error_message}")