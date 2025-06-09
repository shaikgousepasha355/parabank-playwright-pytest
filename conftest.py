import pytest
from playwright.sync_api import sync_playwright
import yaml
import requests
from utils.data_generator import generate_unique_user

@pytest.fixture(scope="session")
def browser_launch_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def api_client():
    return requests.Session()

@pytest.fixture(scope="session")
def unique_user():
    return generate_unique_user()