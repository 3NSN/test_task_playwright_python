import re
from playwright.sync_api import Locator, expect
from pages.base_page import BasePage


class ContentPage(BasePage):
    URL_PATH = "ringtones-and-wallpapers"
    SEARCH_INPUT = "#search"
    WALLPAPER_BTN_HEADER = "a[href='/wallpapers']"

    @property
    def wallpaper_btn_header(self):
        return self.page.locator(self.WALLPAPER_BTN_HEADER).first

    @property
    def search_input(self) -> Locator:
        return self.page.locator(self.SEARCH_INPUT).last

    def type_keyword(self, keyword: str):
        self.search_input.fill(keyword)
        self.page.keyboard.press("Enter")

    def click_wallpaper_btn_header(self):
        return self.wallpaper_btn_header.click()

    def choose_category(self, category_name: str):
        choose_category_btn = self.page.get_by_role("button", name="All", exact=True).last
        choose_category_btn.click()
        self.page.get_by_role("menuitemradio", name=category_name, exact=True).click()


