from .base_page_init import BasePage

class BillPayPage(BasePage):

    def pay_bill(self, payee, amount, from_account):
        self.page.click("#leftPanel > ul > li:nth-child(4) > a")
        self.page.fill('input[name="payee.name"]', payee["name"])
        self.page.fill('input[name="payee.address.street"]', payee["address"])
        self.page.fill('input[name="payee.address.city"]', payee["city"])
        self.page.fill('input[name="payee.address.state"]', payee["state"])
        self.page.fill('input[name="payee.address.zipCode"]', payee["zip_code"])
        self.page.fill('input[name="payee.phoneNumber"]', payee["phone"])
        self.page.fill('input[name="payee.accountNumber"]', payee["account_number"])
        self.page.fill('input[name="verifyAccount"]', payee["account_number"])
        self.page.fill('input[name="amount"]', str(amount))
        self.page.select_option('select[name="fromAccountId"]', from_account)
        self.page.keyboard.press("PageDown")
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press('Tab')
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press('Tab')
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press('Enter')
        if self.page.get_by_text('Error!').is_visible():
            error_message = self.page.inner_text('#billpayError > p')
            raise Exception(f"Bill payment failed: {error_message}")
        else:
            self.page.is_visible('text=Bill Payment Complete')
            return True
    