from faker import Faker
import random

fake = Faker()

def generate_unique_user():
    username = f"{fake.user_name()}_b{random.randint(1000, 9999)}"
    password = fake.password(length=10)
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip_code": fake.zipcode(),
        "phone": fake.phone_number(),
        "ssn": fake.ssn(),
        "username": username,
        "password": password
    }

def payee_details():
    details= {
        "name": fake.name(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip_code": fake.zipcode(),
        "phone": fake.phone_number(),
        "account_number": f"{random.randint(1000000000, 9999999999)}"
    }
    return details