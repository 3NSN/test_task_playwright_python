import re

from playwright.sync_api import expect, Page

from constants import BASE_URL
from pages.content_page import ContentPage


class HomePage(Page):
    URL = BASE_URL

    COOKIE_BTN_PATTERN = re.compile(r"Accept All Cookies|Close", re.IGNORECASE)
    PRIVACY_MODAL = "notice"
    BROWSE_NOW_BTN = "Browse Now"

    def __init__(self, page: Page):
        self.page = page

    def load(self, skip_privacy_dialog: bool = True):
        self.page.goto(self.URL)
        if skip_privacy_dialog:
            try:
                privacy_modal = self.page.get_by_test_id(self.PRIVACY_MODAL)
                accept_btn = privacy_modal.get_by_role("button", name=self.COOKIE_BTN_PATTERN)

                if accept_btn.is_visible(timeout=3000):
                    accept_btn.click()
                    expect(privacy_modal).not_to_be_visible()

            except TimeoutError:
                print("Banner not found or skipped.")
            except Exception as e:
                print(f"Warning during cookie handling: {e}")

    def open_browse_now(self):
        browse_now = self.page.get_by_text(self.BROWSE_NOW_BTN)
        browse_now.click()
        self.page.wait_for_load_state()
        expect(self.page).to_have_url(re.compile(rf".*{ContentPage.URL_PATH}"))
