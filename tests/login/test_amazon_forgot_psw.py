from playwright.sync_api import sync_playwright, expect

import pytest

from pages.login_page import LoginPage

from utils.data_reader import login_data

from utils.config import BASE_URL

#TC_LOGIN_013
@pytest.mark.login
def test_amazon_forgot_psw(page):

    username = login_data["valid_login"]["username"]
    fgusername = login_data["fg_username"]["username"]

    page.goto(BASE_URL, wait_until="domcontentloaded")
        
    login_page = LoginPage(page)

    login_page.sign_other_click()

    login_page.enter_username(username)
    login_page.click_continue()

    login_page.fg_link()
    login_page.fg_username(fgusername)
    login_page.fg_button()
