import os
from pathlib import Path

from playwright.sync_api import Download


def verify_download(download: Download, expected_extensions: tuple = (".jpg", ".png", ".jpeg")) -> Path:
    filename = download.suggested_filename.lower()

    if not any(filename.endswith(ext) for ext in expected_extensions):
        raise AssertionError(f"Invalid file extension: '{filename}'. Expected: {expected_extensions}")

    temp_path = download.path()

    if not temp_path or not os.path.exists(temp_path):
        raise AssertionError("Download failed: temporary file path is missing or invalid.")

    if os.path.getsize(temp_path) == 0:
        raise AssertionError("Downloaded file is empty (0 bytes).")

    return temp_path