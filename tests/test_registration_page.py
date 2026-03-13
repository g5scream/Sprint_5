import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from general_act import Urls, User
from locators import LoginPage, RegPage


class TestRegistrationPage:
    def test_successful_registration(self, browser: WebDriver) -> None:                     # на успешную регистрацию
        user = User.generate()
        browser.get(Urls.reg_page)
        browser.find_element(*RegPage.NAME_INPUT).send_keys(user.name)
        browser.find_element(*RegPage.EMAIL_INPUT).send_keys(user.login)
        browser.find_element(*RegPage.PASSWORD_INPUT).send_keys(user.password)
        browser.find_element(*RegPage.REGISTRATE_BUTTON).click()
        WebDriverWait(browser, 5).until_not(EC.presence_of_element_located(RegPage.REGISTRATE_BUTTON))
        assert browser.current_url == Urls.login_page
        assert browser.find_element(*LoginPage.TITLE_TEXT).is_displayed()

    
    @pytest.mark.parametrize('password', ['1', '123', '1234', '12345'])                     # на ошибку для некорректного пароля
    def test_incorrect_password_error(self, browser: WebDriver, password: str) -> None:
        user = User.generate()
        browser.get(Urls.reg_page)
        browser.find_element(*RegPage.NAME_INPUT).send_keys(user.name)
        browser.find_element(*RegPage.EMAIL_INPUT).send_keys(user.login)
        browser.find_element(*RegPage.PASSWORD_INPUT).send_keys(password)
        browser.find_element(*RegPage.REGISTRATE_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(RegPage.INPUT_ERROR_TEXT))
        error_message = browser.find_element(*RegPage.INPUT_ERROR_TEXT)
        assert error_message.text == 'Некорректный пароль'