import pytest
import configparser
from playwright.sync_api import sync_playwright
from pytest_base_url.plugin import base_url

# getting config.ini
config = configparser.ConfigParser()
config.read("config.ini")

@pytest.fixture(scope="session")
def get_config():
    return config

@pytest.fixture(scope="session")
def browser_context(get_config):
    browser_type = get_config["browser"]["type"]
    headless = get_config["browser"].getboolean("headless")
    slow_mo = get_config["browser"].getint("slow-mo")
    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=headless, slow_mo=slow_mo)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=headless, slow_mo=slow_mo)
        elif browser_type == "webkit":
            browser = p.webkit.launch(headless=headless, slow_mo=slow_mo)
        else:
            raise ValueError(f"Not supported browser.")
        context = browser.new_context()
        yield context
        browser.close()

@pytest.fixture(scope="session")
def page(browser_context,get_config):
    page = browser_context.new_page()
    page.goto(get_config["environment"]["base_url"])
    yield page
    page.close()

@pytest.fixture(scope="function")
def login_details(get_config):
    return {
        "valid_username": get_config["login_details"]["valid_username"],
        "valid_password": get_config["login_details"]["valid_password"],
        "invalid_username":get_config["login_details"]["invalid_username"],
        "invalid_password":get_config["login_details"]["invalid_password"]
    }