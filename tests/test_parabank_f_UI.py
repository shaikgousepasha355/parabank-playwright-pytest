import pytest
import json
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.transfer_page import TransferPage
from pages.billpay_page import BillPayPage
from faker import Faker

fake = Faker()

@pytest.mark.order(1)
def test_e2e_ui(browser_launch_context, config, unique_user):
    try:    
        page = browser_launch_context.new_page()
        # 1. Navigate to Para bank application
        register = RegistrationPage(page, config)
        register.Navigate()
        # 2. Create new user by registration
        register.register(unique_user)
        assert register.registration_successful(), "Registration failed"
        page.wait_for_timeout(2000)

        # 3. Login with new user
        page.get_by_text('Log Out').click()  # logging out the session before login
        login_page = LoginPage(page)

        login_page.login(unique_user["username"], unique_user["password"])
        page.wait_for_timeout(3000)
        assert login_page.is_logged_in(), "Login failed"

        # 4. Verify global navigation menu
        home_page = HomePage(page)
        home_page.global_nav_menu_check()

        # 5. Create a Savings account
        account_page = AccountPage(page)
        new_account_id = account_page.open_new_savings_account()
        assert new_account_id.isdigit(), "Account creation failed"
        
        # 6. Validate Accounts overview page
        balance = account_page.get_account_balance(new_account_id)
        assert balance == 500, "Account balance not displayed"

        # 7. Transfer funds to another account from new account of step 5
        transfer_page = TransferPage(page)
        transfer_page.Navigation()
        page.wait_for_timeout(2000)
        assert transfer_page.transfer_funds(5, new_account_id), "Fund transfer failed"

        # 8. Pay bill with new account
        payee = {
            "name": fake.name(),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip_code": fake.zipcode(),
            "phone": fake.phone_number(),
            "account_number": f"{fake.random_int(min=1000000000, max=9999999999)}"
        }
        billpay = BillPayPage(page)
        billpay.pay_bill(payee, 5, new_account_id)

        # Save relevant info to integrate in API test
        page.context.storage_state(path="utils/user_state.json")
        page.context.add_cookies(page.context.cookies())
        with open("utils/account_info.json", "w") as f:
            json.dump({"account_id": new_account_id}, f)
    except Exception as e:
        page.screenshot(path="utils/error_screenshot.png")
        raise e
    finally:
        page.close()    

     