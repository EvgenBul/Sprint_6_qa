import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait

class TestLogo:
    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат" в шапке')
    def test_logo_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_element(MainPageLocators.header_logo_scooter)
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_dzen(self, driver):
        main_page = MainPage(driver)

        with allure.step('1. Открыть главную страницу'):
            main_page.open()

        with allure.step('2. Кликнуть на логотип Яндекс'):
            main_page.wait_visibility_of_header_logo_yandex()
            main_page.click_on_header_logo_yandex()

        with allure.step('3. Переключиться и проверить заголовок'):
            # Ждем появления второй вкладки
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            main_page.switch_to_next_tab()

            # Явное ожидание загрузки title
            WebDriverWait(driver, 10).until(
                lambda d: d.title != '' and 'Дзен' in d.title,
                message=f'Заголовок не содержит "Дзен". Текущий заголовок: {driver.title}'
            )
