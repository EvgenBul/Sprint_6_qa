import allure
from conftest import driver
from pages.main_page import MainPage


class TestLogoYandex:
    @allure.title('Переход на главную страницу при нажатии на логотип "Самокат"')
    def test_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_order_button_in_header()
        main_page.click_order_button_in_header()
        main_page.wait_visibility_header_logo_scooter()
        main_page.click_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Переход на страницу "Дзена" при нажатии на логотип "Яндекс"')
    def test_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_logo_yandex()
        main_page.click_on_logo_yandex()
        main_page.switch_to_next_tab()
        assert 'Дзен' in main_page.get_page_title()