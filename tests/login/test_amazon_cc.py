from playwright.sync_api import sync_playwright, expect
import pytest

from utils.data_reader import login_data

from pages.login_page import LoginPage

from utils.config import BASE_URL

# TC_LOGIN_004
# Verify that mobile or email field is empty
# 1. Open amazon 2. Click sign in 3. Field like empty 4. Click Continue

@pytest.mark.login
def test_amazon_country_code(page):
    country_code = login_data["country_code"]["username"]

    page.goto(BASE_URL, wait_until="domcontentloaded")

    login_page = LoginPage(page)

    login_page.sign_in_click()
    login_page.enter_username(country_code)
    login_page.click_continue()

    # error_message = page.get_by_text("Invalid mobile number").inner_text()
    # print(f"TC_LOGIN_006 Error message: {error_message}")

    expect(page.get_by_text("Invalid mobile number")).to_be_visible()