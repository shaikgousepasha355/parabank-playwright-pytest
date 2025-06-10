from .base_page_init import BasePage

class AccountPage(BasePage):
    def open_new_savings_account(self, account_type="SAVINGS"):
        self.page.goto("https://parabank.parasoft.com/parabank/openaccount.htm")
        self.page.select_option('select#type', account_type)
        text = self.page.inner_text('b:has-text("A minimum of $")')
        minimum_amount_transferred = None
        for x in text.split():
            if x.startswith('$'):
                amount = x[1:].split('.')[0].replace(',', '')
                if amount.isdigit():
                    minimum_amount_transferred = int(amount)
                    break
        if minimum_amount_transferred is None:
            raise ValueError("Minimum amount to transfer not found in the text.")
        press_tab = lambda n: [self.page.keyboard.press('Tab') for _ in range(n)]
        press_tab(21)
        self.page.timeout = 3000
        self.page.keyboard.press('Enter')
        self.page.wait_for_selector('a#newAccountId')
        account_id = self.page.inner_text('a#newAccountId')
        return account_id, minimum_amount_transferred

    def get_account_balance(self, account_id):
        self.page.click(f'text={account_id}')
        self.page.wait_for_timeout(3000)
        balance = self.page.inner_text('td#balance')
        return float(balance.replace('$', ''))