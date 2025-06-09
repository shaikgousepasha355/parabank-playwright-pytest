
class RegistrationPage():
    def __init__(self, page,config):
        self.page = page
        self.config = config

    def Navigate(self):
        self.page.goto(self.config["UI"]["base_url"])

    def register(self, user):
        self.page.locator('#loginPanel > p:nth-child(3) > a').click()
        self.page.fill('input[name="customer.firstName"]', user["first_name"])
        self.page.fill('input[name="customer.lastName"]', user["last_name"])
        self.page.fill('input[name="customer.address.street"]', user["address"])
        self.page.fill('input[name="customer.address.city"]', user["city"])
        self.page.fill('input[name="customer.address.state"]', user["state"])
        self.page.fill('input[name="customer.address.zipCode"]', user["zip_code"])
        self.page.fill('input[name="customer.phoneNumber"]', user["phone"])
        self.page.fill('input[name="customer.ssn"]', user["ssn"])
        self.page.fill('input[name="customer.username"]', user["username"])
        self.page.fill('input[name="customer.password"]', user["password"])
        self.page.fill('input[name="repeatedPassword"]', user["password"])
        self.page.click('input[value="Register"]')
        self.page.wait_for_timeout(3000)

    def registration_successful(self):
        return self.page.is_visible('text=Your account was created successfully. You are now logged in.')