import re
from playwright.sync_api import Locator, expect
from pages.base_page import BasePage


class WallpaperPage(BasePage):
    URL_PATH = "wallpapers"
    CONTENT_ITEMS = "div[class*='CardsContainer'] a"
    PREMIUM_ICON = "span[data-icon='true']"
    DOWNLOAD_BTN_NAME = "Download"
    MODAL_TEXT = "Preparing your download"


    @property
    def content_items(self) -> Locator:
        return self.page.locator(self.CONTENT_ITEMS)

    @property
    def premium_icon(self) -> Locator:
        return self.page.locator(self.PREMIUM_ICON)

    @property
    def download_modal(self) -> Locator:
        return self.page.get_by_text(self.MODAL_TEXT)

    def click_first_free_item(self):
        free_item = self.content_items.filter(has_not=self.premium_icon).first

        if not free_item.is_visible():
            raise Exception("Free items not found!")

        free_item.click()

        if self.handle_google_vignette():
            free_item.click()

    def download_file_and_wait(self):
        self.page.get_by_role("button", name=self.DOWNLOAD_BTN_NAME).click()
        expect(self.download_modal).to_be_visible(timeout=5000)
        expect(self.download_modal).not_to_be_visible(timeout=45000)

    def verify_premium_and_free_items_exist(self):
        premium_items = self.content_items.filter(has=self.premium_icon)
        free_items = self.content_items.filter(has_not=self.premium_icon)
        expect(premium_items.first).to_be_visible()
        expect(free_items.first).to_be_visible()
        print(f"Verified: Found {premium_items.count()} premium and {free_items.count()} free items.")
