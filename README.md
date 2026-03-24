# Sprint_5

UI‑тестирование сервиса [Stellar Burgers](https://stellarburgers.education-services.ru) в браузере Google Chrome.

## Стек технологий

* **Язык:** Python.
* **Фреймворк:** PyTest.
* **Автоматизация:** Selenium WebDriver.
* **Архитектура:** Page Object Model (локаторы вынесены в отдельные модули).
* **Запуск тестов в один поток:** `pytest -v`.

## Структура проекта

### Основные модули

**1. [`conftest.py`](conftest.py)** — предоставляет фикстуры для настройки окружения тестов:
* `browser` — создаёт и настраивает экземпляр браузера Chrome для каждого теста.
* `registered_user` (`scope="session"`) — регистрирует одного пользователя на всю сессию тестов (избегает повторной регистрации).
* `login` — авторизует пользователя перед тестом и возвращает авторизованный браузер.

**2. [`general_act.py`](general_act.py)** предоставляет:
* `class Urls` — URL‑адреса всех страниц приложения в едином месте.
* `class User` — генерирует случайных тестовых пользователей для изолированных тестов.
* `class StaticUser` — работает со статическими данными пользователя (логин, пароль, имя) для сценариев с фиксированными данными.
* методы регистрации и проверки статуса — автоматизирует подготовку окружения, проверяет, нужно ли регистрировать пользователя, и выполняет регистрацию при необходимости.

**3. [`locators.py`](locators.py)** содержит:
* локаторы элементов веб‑интерфейса - локаторы сгруппированы по страницам приложения в виде классов.

### Папка `tests/` — содержит тесты проекта

**1. Регистрация [test_registration_page.py](tests/test_registration_page.py):**
* `test_successful_registration` — тест успешной регистрации.
* `test_incorrect_password_error` — тестирует валидацию пароля (с параметризацией: пароли разной длины).

**Запуск:** `pytest -v tests/test_registration_page.py`

**2. Вход в систему [test_login_page.py](tests/test_login_page.py):** проверяет авторизацию через разные точки входа:
* `test_login_via_login_button_show_main_page` — через кнопку «Войти в аккаунт» на главной странице.
* `test_login_via_profile_show_main_page` — через кнопку «Личный кабинет».
* `test_login_via_registration_page_show_main_page` — вход через кнопку в форме регистрации.
* `test_login_via_recover_pass_page_show_main_page` — вход через кнопку в форме восстановления пароля.

**Запуск:** `pytest -v tests/test_login_page.py`

**3. Личный кабинет [test_profile_page.py](tests/test_profile_page.py):** тестирует навигацию и функционал профиля:
* `test_click_profile_link_open_profile_page` — переход по клику на «Личный кабинет».
* `test_click_constructor_link_show_constructor` — переход по клику на «Конструктор».
* `test_click_main_logo_show_constructor` — переход на главную по клику на логотип Stellar Burgers.
* `test_click_logout_button_show_login_page` — выход по кнопке «Выйти» в личном кабинете.

**Запуск:** `pytest -v tests/test_profile_page.py`

**4. Раздел «Конструктор» [test_constructor_section.py](tests/test_constructor_section.py):** проверяет переключение между разделами конструктора бургеров:
* «Булки» — тест `test_click_buns_scroll_to_buns`.
* «Соусы» — тест `test_click_sauces_scroll_to_sauces`.
* «Начинки» — тест `test_click_fillings_scroll_to_fillings`.

**Запуск:** `pytest -v tests/test_constructor_section.py`
