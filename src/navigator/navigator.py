from time import sleep

from playwright.sync_api import sync_playwright

from .utils.constants import URL


class Navigator:
    def __init__(self, headless: bool = False):
        """Navigator class constructor

        Args:
            headless (bool, optional): run the browser in headless mode. Defaults to False.
        """
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=headless)

    def run(self, username: str, password: str):
        """Run the navigator

        Args:
            username (str): username to login with
            password (str): password to login with
        """
        page = self.browser.new_page()
        page.goto(URL)
        page.get_by_text("Efrei Paris", exact=True).click()
        page.locator("#username").fill(username)
        page.locator("#password").fill(password)
        page.locator("button[type='submit']").click()
        page.get_by_text("Etudes et scolarité").nth(0).click()
        page.get_by_text("Student services").nth(0).click()

        all_excel_files = page.get_by_text("TABLEAUX D'EXAMENS")
        with page.expect_download() as download_info:
            for i in range(all_excel_files.count()):
                all_excel_files.nth(i).click()
                download_info.value.save_as(f"tmp/tableau_{i}.xlsx")

        self.browser.close()
