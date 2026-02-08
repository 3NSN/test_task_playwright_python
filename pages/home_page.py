import re

from playwright.sync_api import expect, Page

from constants import BASE_URL
from pages.content_page import ContentPage


class HomePage(Page):
    URL = BASE_URL

    ACCEPT_ALL_COOKIES_BTN = "Accept All Cookies"
    PRIVACY_MODAL = "notice"
    BROWSE_NOW_BTN = "Browse Now"

    def __init__(self, page: Page):
        self.page = page


    def load(self, skip_privacy_dialog: bool = True):
        self.page.goto(self.URL)

        if skip_privacy_dialog:
            try:
                privacy_modal = self.page.get_by_test_id(self.PRIVACY_MODAL)
                accept_btn = privacy_modal.get_by_label(self.ACCEPT_ALL_COOKIES_BTN)
                accept_btn.wait_for(state="visible", timeout=3000)
                accept_btn.click()
                expect(privacy_modal).not_to_be_visible()
            except Exception:
                print("GDPR Banner not found or skipped.")


    def open_browse_now(self):
        browse_now = self.page.get_by_text(self.BROWSE_NOW_BTN)
        browse_now.click()
        self.page.wait_for_load_state()
        expect(self.page).to_have_url(re.compile(fr".*{ContentPage.URL_PATH}"))
