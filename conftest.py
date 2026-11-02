import pytest

from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

#pytest fixture to launch a browser instance
@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()