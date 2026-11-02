from playwright.sync_api import sync_playwright


def dismiss_google_popups(page):
    page.context.on("page", lambda popup: popup.close())

    selectors = [
        "button:has-text('Reject all')",
        "button:has-text('Accept all')",
        "button:has-text('No thanks')",
        "button:has-text('I agree')",
        "button:has-text('Accept')",
        "button:has-text('Close')",
    ]

    for selector in selectors:
        try:
            locator = page.locator(selector).first
            if locator.is_visible(timeout=1000):
                locator.click()
                page.wait_for_timeout(500)
        except Exception:
            pass


def test_google_page_title_and_content():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com", wait_until="domcontentloaded")
        dismiss_google_popups(page)
        #page.wait_for_timeout(1000)

        title = page.title()
        body_text = page.locator("body").inner_text()

        assert "Google" in title, f"Expected Google in page title, got: {title}"
        assert "Google" in body_text, f"Expected Google text on the page, got: {body_text[:200]}"

        browser.close()
