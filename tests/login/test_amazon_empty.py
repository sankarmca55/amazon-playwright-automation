import pytest
from utils.data_reader import login_data
from pages.login_page import LoginPage

from utils.config import BASE_URL

@pytest.mark.login
def test_amazon_empty_field(page):

    empty_user_name = login_data["empty_username"]["username"]

    page.goto(BASE_URL, wait_until="domcontentloaded")

    login_page = LoginPage(page)

    login_page.sign_other_click()
    login_page.enter_username(empty_user_name)
    login_page.click_continue()

    page.wait_for_timeout(2000)

    error_message = page.get_by_text(
        "Enter your mobile number or email"
    ).inner_text()

    print(f"TC_LOGIN_004 Error message: {error_message}")