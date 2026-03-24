from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import MainPage


class TestConstructorSection:
    def test_click_buns_scroll_to_buns(self, login: WebDriver) -> None:
        browser = login
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable(MainPage.CONSTRUCTOR_LINK_TEXT)).click()
        wait.until(EC.element_to_be_clickable(MainPage.FILLINGS_TAB)).click()
        buns_tab = wait.until(EC.element_to_be_clickable(MainPage.BUNS_TAB))
        buns_tab.click()
        wait.until(EC.text_to_be_present_in_element_attribute(MainPage.BUNS_TAB, 'class', MainPage.ACTIVE_TAB_CLASS))
        assert MainPage.ACTIVE_TAB_CLASS in buns_tab.get_attribute('class')

    def test_click_sauces_scroll_to_sauces(self, login: WebDriver) -> None:
        browser = login
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable(MainPage.CONSTRUCTOR_LINK_TEXT)).click()
        sauces_tab = wait.until(EC.element_to_be_clickable(MainPage.SAUCES_TAB))
        sauces_tab.click()
        wait.until(EC.text_to_be_present_in_element_attribute(MainPage.SAUCES_TAB, 'class', MainPage.ACTIVE_TAB_CLASS))
        assert MainPage.ACTIVE_TAB_CLASS in sauces_tab.get_attribute('class')

    def test_click_fillings_scroll_to_fillings(self, login: WebDriver) -> None:
        browser = login
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable(MainPage.CONSTRUCTOR_LINK_TEXT)).click()
        fillings_tab = wait.until(EC.element_to_be_clickable(MainPage.FILLINGS_TAB))
        fillings_tab.click()
        wait.until(EC.text_to_be_present_in_element_attribute(MainPage.FILLINGS_TAB, 'class', MainPage.ACTIVE_TAB_CLASS))
        assert MainPage.ACTIVE_TAB_CLASS in fillings_tab.get_attribute('class')