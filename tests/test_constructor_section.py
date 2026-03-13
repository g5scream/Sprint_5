from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import MainPage


class TestConstructorSection:
    def test_click_buns_scroll_to_buns(self, login: WebDriver) -> None:
        browser = login
        browser.find_element(*MainPage.CONSTRUCTOR_LINK_TEXT).click()
        browser.find_element(*MainPage.FILLINGS_TAB).click()
        browser.find_element(*MainPage.BUNS_TAB).click()
        sleep(1)
        buns_tab_class = browser.find_element(*MainPage.BUNS_TAB).get_attribute('class')
        assert buns_tab_class is not None and MainPage.ACTIVE_TAB_CLASS in buns_tab_class

    def test_click_sauces_scroll_to_sauces(self, login: WebDriver) -> None:
        browser = login
        browser.find_element(*MainPage.CONSTRUCTOR_LINK_TEXT).click()
        browser.find_element(*MainPage.SAUCES_TAB).click()
        sleep(1)
        sauses_tab_class = browser.find_element(*MainPage.SAUCES_TAB).get_attribute('class')
        assert sauses_tab_class is not None and MainPage.ACTIVE_TAB_CLASS in sauses_tab_class

    def test_click_fillings_scroll_to_fillings(self, login: WebDriver) -> None:
        browser = login
        browser.find_element(*MainPage.CONSTRUCTOR_LINK_TEXT).click()
        browser.find_element(*MainPage.FILLINGS_TAB).click()
        sleep(1)
        fillings_tab_class = browser.find_element(*MainPage.FILLINGS_TAB).get_attribute('class')
        assert fillings_tab_class is not None and MainPage.ACTIVE_TAB_CLASS in fillings_tab_class