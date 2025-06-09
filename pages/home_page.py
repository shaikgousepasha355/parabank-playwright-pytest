from conftest import config
from .base_page_init import BasePage

class HomePage(BasePage):
   
    def global_nav_menu_check(self):
        navigation_links = [
            ('#leftPanel > ul > li:nth-child(1) > a', 'openaccount'),
            ('#leftPanel > ul > li:nth-child(2) > a', 'overview'),
            ('#leftPanel > ul > li:nth-child(3) > a', 'transfer'),
            ('#leftPanel > ul > li:nth-child(4) > a', 'billpay'),
            ('#leftPanel > ul > li:nth-child(5) > a', 'findtrans'),
            ('#leftPanel > ul > li:nth-child(6) > a', 'updateprofile')
        ]
        for link_text, url_part in navigation_links:
            self.page.locator(link_text).click()
            assert url_part in self.page.url, f"Navigation to {link_text} failed"