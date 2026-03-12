import pytest
from typing import Any, Generator
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from general_act import Urls, StaticUser
from locators import LoginPage, MainPage


@pytest.fixture
def browser() -> Generator[WebDriver, Any, None]:
    browser = webdriver.Chrome()
    browser.get(Urls.main_page)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def registered_user() -> StaticUser:
    user = StaticUser.get_static()
    temp_browser = webdriver.Chrome()
    try:
        StaticUser.register(temp_browser, user)
        return user
    finally:
        temp_browser.quit()


@pytest.fixture
def login(browser: WebDriver) -> WebDriver:
    browser.get(Urls.login_page)
    browser.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
    browser.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
    browser.find_element(*LoginPage.LOGIN_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))
    return browser