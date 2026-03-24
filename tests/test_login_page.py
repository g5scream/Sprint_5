from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from general_act import Urls, StaticUser
from locators import LoginPage, MainPage, RegPage


class TestLoginPage:
    def test_login_via_login_button_show_main_page(self, browser: WebDriver, registered_user: StaticUser) -> None:  # вход по кнопке «Войти в аккаунт» на главной
        browser.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        browser.find_element(*LoginPage.EMAIL_FIELD).send_keys(registered_user.LOGIN)
        browser.find_element(*LoginPage.PASSWORD_FIELD).send_keys(registered_user.PASSWORD)
        browser.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert browser.current_url == Urls.main_page and browser.find_element(*MainPage.ORDER_BUTTON)

    def test_login_via_profile_show_main_page(self, browser: WebDriver) -> None:                                    # вход через кнопку «Личный кабинет»
        browser.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        browser.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
        browser.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
        browser.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert browser.current_url == Urls.main_page and browser.find_element(*MainPage.ORDER_BUTTON)

    def test_login_via_registration_page_show_main_page(self, browser: WebDriver) -> None:                          # вход через кнопку в форме регистрации
        browser.get(Urls.reg_page)
        browser.find_element(*RegPage.LOGIN_TEXT_WITH_HREF).click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        browser.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
        browser.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
        browser.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert browser.current_url == Urls.main_page and browser.find_element(*MainPage.ORDER_BUTTON)

    def test_login_via_recover_pass_page_show_main_page(self, browser: WebDriver) -> None:                          # вход через кнопку в форме восстановления пароля.
        browser.get(Urls.recover_pass_page)
        browser.find_element(*LoginPage.LOGIN_TEXT_WITH_HREF).click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        browser.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
        browser.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
        browser.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(browser, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert browser.current_url == Urls.main_page and browser.find_element(*MainPage.ORDER_BUTTON)