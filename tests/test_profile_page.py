from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from general_act import Urls
from locators import LoginPage, MainPage, ProfilePage

class TestProfilePage:

    def test_click_profile_link_open_profile_page(self, login: WebDriver) -> None:                                # Проверен переход по клику на «Личный кабинет»
        browser = login
        browser.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        assert browser.current_url == Urls.profile_page
        info_element = browser.find_element(*ProfilePage.INFO_TEXT)
        assert info_element.is_displayed()

    def test_click_constructor_link_show_constructor(self, login: WebDriver) -> None:                             # Проверен переход по клику на «Конструктор»
        browser = login
        browser.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        browser.find_element(*ProfilePage.CONSTRUCTOR_LINK_TEXT).click()
        h1_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProfilePage.H1_TITLE))
        assert h1_element.text == 'Соберите бургер'

    def test_click_main_logo_show_constructor(self, login: WebDriver) -> None:                                    # Проверен переход по клику на логотип Stellar Burgers.
        browser = login
        browser.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        browser.find_element(*ProfilePage.MAIN_LOGO).click()
        h1_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProfilePage.H1_TITLE))
        assert h1_element.text == 'Соберите бургер'

    def test_click_logout_button_show_login_page(self, login: WebDriver) -> None:                                 # Проверь выход по кнопке «Выйти» в личном кабинете.
        browser = login
        browser.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        browser.find_element(*ProfilePage.LOGOUT_BUTTON).click()
        WebDriverWait(browser, 10).until_not(EC.presence_of_element_located(ProfilePage.LOGOUT_BUTTON))
        title_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LoginPage.TITLE_TEXT))
        assert browser.current_url == Urls.login_page
        assert title_element.is_displayed()