import pytest

from pages.home_page import HomePage
from pages.content_page import ContentPage
from pages.wallpaper_page import WallpaperPage


@pytest.fixture(scope='function')
def browser_context(browser):
    with browser.new_context() as browser_context:
        yield browser_context


@pytest.fixture(scope='function')
def base_page(browser_context):
    return browser_context.new_page()


@pytest.fixture(scope="function")
def home_page(base_page):
    return HomePage(base_page)


@pytest.fixture(scope="function")
def content_page(base_page):
    return ContentPage(base_page)

@pytest.fixture(scope="function")
def wallpaper_page(base_page):
    return WallpaperPage(base_page)