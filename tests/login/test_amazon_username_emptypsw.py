from playwright.sync_api import sync_playwright, expect

import pytest
from utils.data_reader import login_data

from pages.login_page import LoginPage

from utils.config import BASE_URL

@pytest.mark.login
def test_amazon_validuser_empty_psw(page):
    valid_user = login_data["empty_password"]["username"]
    empty_password = login_data["empty_password"]["password"]

    page.goto(BASE_URL, wait_until="domcontentloaded")

    login_page = LoginPage(page)

    login_page.sign_other_click()
    login_page.enter_username(valid_user)
    login_page.click_continue()
    login_page.enter_password(empty_password)
    login_page.click_sign_in()

    error_message = page.get_by_text("Enter your password").inner_text()
    print(f"TC_LOGIN_012 Error message: {error_message}")