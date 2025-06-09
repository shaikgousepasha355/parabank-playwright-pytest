from .base_page_init import BasePage

class TransferPage(BasePage):
    def Navigation(self):
        self.page.click("#leftPanel > ul > li:nth-child(3) > a")

    def transfer_funds(self, amount, from_account):
        self.page.fill('input[id="amount"]', str(amount))
        self.page.select_option('select[id = "fromAccountId"]', from_account)
        press_tab = lambda n: [self.page.keyboard.press('Tab') for _ in range(n)]
        press_tab(3)
        self.page.keyboard.press('Enter')
        self.page.wait_for_timeout(2000)
        return self.page.is_visible('text=Transfer Complete!')