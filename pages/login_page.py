from .base_page_init import BasePage

class LoginPage(BasePage):

    def login(self, username, password):
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('input[value="Log In"]')

    def is_logged_in(self):
        return self.page.is_visible('text=Accounts Overview')