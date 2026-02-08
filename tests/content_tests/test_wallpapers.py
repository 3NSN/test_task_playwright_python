from time import sleep

from constants import CategoryNames
from helpers.assert_utils import verify_download


def test_searching_wallpapers_by_keyword(home_page, content_page, wallpaper_page):
    home_page.load()
    sleep(5)
    home_page.open_browse_now()
    content_page.choose_category(CategoryNames.WALLPAPERS)
    content_page.type_keyword_and_search("Cat")
    wallpaper_page.verify_search_header("Cat Wallpapers")
    wallpaper_page.click_first_free_item()
    wallpaper_page.verify_search_header("Cat")


def test_download_wallpaper(home_page, content_page, wallpaper_page,browser_type_launch_args):

    home_page.load()
    home_page.open_browse_now()
    content_page.choose_category(CategoryNames.WALLPAPERS)
    content_page.type_keyword_and_search("Cat")
    wallpaper_page.verify_search_header("Cat Wallpapers")
    wallpaper_page.click_first_free_item()
    with wallpaper_page.page.expect_download() as download_info:
        wallpaper_page.download_file_and_wait()
    
    download = download_info.value
    verify_download(download)

def test_free_and_prem_wallpaper_exists(home_page, content_page, wallpaper_page):
    home_page.load()
    home_page.open_browse_now()
    content_page.choose_category(CategoryNames.WALLPAPERS)
    content_page.type_keyword_and_search("Cat")
    wallpaper_page.verify_premium_and_free_items_exist()
