from playwright.sync_api import sync_playwright, expect

import pytest

from utils.data_reader import login_data

from pages.login_page import LoginPage
from utils.config import BASE_URL

@pytest.mark.login
def test_amazon_login(page):
    valid_username = login_data["valid_login"]["username"]
    valid_password = login_data["valid_login"]["password"]

    page.goto(BASE_URL, wait_until="domcontentloaded")

    login_page = LoginPage(page)

    login_page.sign_in_click()

    login_page.enter_username(valid_username)
    login_page.click_continue()
    login_page.enter_password(valid_password)
    login_page.click_sign_in()