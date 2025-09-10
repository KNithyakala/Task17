from playwright.sync_api import Page
from playwright.sync_api import TimeoutError


class Dashboard():
    def __init__(self,page):
        self.launch_alert = page.locator("//button[contains(text(),'✕')]")
        self.welcome_block= page.locator("//div[@class='header-left-part']/p")
        self.profile      = page.locator('//img[@id="profile-click-icon"]')
        self.logout       = page.locator('//div[text()="Log out"]')

    def get_welcome_message(self):
        try:
            self.welcome_block.wait_for(timeout=3000)
            return self.welcome_block.inner_text()
        except TimeoutError:
            return None

    def click_logout(self):
        if self.launch_alert.is_visible:
            self.launch_alert.click()
        try:
            self.profile.wait_for(timeout=3000)
            self.profile.click()
            self.logout.is_visible()
            self.logout.click()
            return True
        except TimeoutError as e:
            print(f"[ERROR] failed to click logout button. Exception: {e}")