import random
import string
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPage, RegPage, MainPage

SERVICE_BASE_URL = 'https://stellarburgers.education-services.ru'

class Urls:
    reg_page = f'{SERVICE_BASE_URL}/register'
    main_page = f'{SERVICE_BASE_URL}/'
    login_page = f'{SERVICE_BASE_URL}/login'
    profile_page = f'{SERVICE_BASE_URL}/account/profile'
    recover_pass_page = f'{SERVICE_BASE_URL}/forgot-password'
    order_history_page = f'{SERVICE_BASE_URL}/account/order-history'


class User:
    def __init__(self, name: str, login: str, password: str) -> None:
        self.name = name
        self.login = login
        self.password = password

    @classmethod
    def generate(cls, length: int = 6):
        name = f'Evgen{random.randint(100, 999)}'
        number = random.randint(100, 999)
        login = f'EvgeniiR_39_{number}@yandex.ru'
        characters = string.ascii_lowercase + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return cls(name=name, login=login, password=password)
    

class StaticUser:                                                                  # эксперементировал для себя, с проверкой уже на зареганного 
    LOGIN = "Еvgenii_test@yandex.ru"
    PASSWORD = "test123"
    NAME = "EvgenTest"
    
    @classmethod
    def get_static(cls) -> 'StaticUser':
        return cls(cls.LOGIN, cls.PASSWORD, cls.NAME)

    @classmethod
    def is_registered(cls, browser: WebDriver, user: 'StaticUser') -> bool:
        try:
            browser.get(Urls.login_page)
            browser.find_element(*LoginPage.EMAIL_FIELD).send_keys(user.login)
            browser.find_element(*LoginPage.PASSWORD_FIELD).send_keys(user.password)
            browser.find_element(*LoginPage.LOGIN_BUTTON).click()
            WebDriverWait(browser, 5).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))
            return True
        except Exception:
            return False
    
    @classmethod
    def register(cls, browser: WebDriver, user: 'StaticUser') -> None:            # Регистрирует пользователя, если он ещё не зарегистрирован.             
        if cls.is_registered(browser, user):
            return

        browser.get(Urls.reg_page)
        browser.find_element(*RegPage.NAME_INPUT).send_keys(user.name)
        browser.find_element(*RegPage.EMAIL_INPUT).send_keys(user.login)
        browser.find_element(*RegPage.PASSWORD_INPUT).send_keys(user.password)
        browser.find_element(*RegPage.REGISTRATE_BUTTON).click()

        WebDriverWait(browser, 5).until(EC.presence_of_element_located(RegPage.REGISTRATE_BUTTON))

    def __init__(self, login: str, password: str, name: str):
        self.login = login
        self.password = password
        self.name = name