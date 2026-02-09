from playwright.sync_api import Page, expect
import re


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_search_results_url(self, keyword: str):
        pattern = re.compile(rf".*wallpapers\?keyword={keyword}")
        expect(self.page).to_have_url(pattern)

    def verify_search_header(self, keyword: str):
        expected_text = f"{keyword.title()}"
        expect(self.page.get_by_text(expected_text).first).to_be_visible()

    def handle_google_vignette(self):
        try:
            self.page.wait_for_url("**/*google_vignette", timeout=2000)
            self.page.go_back()
            self.page.wait_for_load_state("domcontentloaded")
            return True
        except Exception:
            return False
