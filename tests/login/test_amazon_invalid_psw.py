from playwright.sync_api import sync_playwright, expect

import pytest
from utils.data_reader import login_data

from pages.login_page import LoginPage

from utils.config import BASE_URL

@pytest.mark.login
def test_amazon_login_invalid_psw(page):

    valid_username = login_data["valid_login"]["username"]
    invalid_pass = login_data["invalid_password"]["password"]

    page.goto(BASE_URL, wait_until="domcontentloaded")

    login_page = LoginPage(page)

    login_page.sign_other_click()

    login_page.enter_username(valid_username)
    login_page.click_continue()

    login_page.enter_password(invalid_pass)
    login_page.click_sign_in()
    error_message = page.get_by_text("Your password is incorrect").inner_text()
    print(f"TC_LOGIN_010 Error message: {error_message}")

