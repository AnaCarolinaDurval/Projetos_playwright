import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def setup_test(page: Page, playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    context = browser.new_context(base_url="https://bugbank.netlify.app/", viewport={"width": 1600, "height": 1200})
    page = context.new_page()

    yield page

    browser.close()