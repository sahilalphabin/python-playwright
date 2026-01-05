"""
Test suite for pytest-playwright-json reporter.
10 failing tests, 5 passing tests.
"""

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"


class TestPassing:
    """5 tests that pass."""

    def test_page_title(self, page: Page) -> None:
        page.goto(BASE_URL)
        expect(page).to_have_title("Swag Labs")

    def test_login_form_visible(self, page: Page) -> None:
        page.goto(BASE_URL)
        expect(page.locator("#user-name")).to_be_visible()

    def test_login_button_enabled(self, page: Page) -> None:
        page.goto(BASE_URL)
        expect(page.locator("#login-button")).to_be_enabled()

    def test_successful_login(self, page: Page) -> None:
        page.goto(BASE_URL)
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        expect(page).to_have_url(f"{BASE_URL}inventory.html")

    def test_screenshot_capture(self, page: Page) -> None:
        page.goto(BASE_URL)
        screenshot = page.screenshot()
        assert len(screenshot) > 0


class TestFailing:
    """10 tests that fail."""

    def test_wrong_title(self, page: Page) -> None:
        page.goto(BASE_URL)
        expect(page).to_have_title("Wrong Title")

    def test_element_not_found(self, page: Page) -> None:
        page.goto(BASE_URL)
        expect(page.locator("#missing")).to_be_visible(timeout=1000)

    def test_assertion_error(self, page: Page) -> None:
        page.goto(BASE_URL)
        assert 1 == 2

    def test_index_error(self, page: Page) -> None:
        page.goto(BASE_URL)
        _ = [1, 2][10]

    def test_key_error(self, page: Page) -> None:
        page.goto(BASE_URL)
        _ = {}["missing"]

    def test_type_error(self, page: Page) -> None:
        page.goto(BASE_URL)
        _ = "str" + 1

    def test_zero_division(self, page: Page) -> None:
        page.goto(BASE_URL)
        _ = 1 / 0

    def test_wrong_url(self, page: Page) -> None:
        page.goto(BASE_URL)
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        expect(page).to_have_url("https://wrong.url")

    def test_missing_element(self, page: Page) -> None:
        page.goto(BASE_URL)
        expect(page.locator("#nonexistent")).to_be_visible()

    def test_screenshot_fail(self, page: Page) -> None:
        page.goto(BASE_URL)
        screenshot = page.screenshot()
        assert len(screenshot) == 12345
