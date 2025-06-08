# main_page.py
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.step('Подождать прогрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('Подождать прогрузки логотипа "Самокат"')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('Кликнуть на логотип "Самокат"')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Подождать прогрузки главного заголовка')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверить отображение главного заголовка')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Подождать прогрузки логотипа "Яндекс"')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Кликнуть на логотип "Яндекс"')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('Переключиться на следующую вкладку')
    def switch_to_next_tab(self):
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            self.driver.switch_to.window(window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        return self.driver.title

    @allure.step('Кликнуть на логотип Яндекс и переключиться')
    def click_yandex_logo_and_switch(self):
        self.wait_visibility_of_header_logo_yandex()
        self.click_on_header_logo_yandex()
        self.switch_to_next_tab()

    @allure.step('Дождаться заголовка Дзена')
    def wait_for_dzen_title(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.title != '' and 'Дзен' in d.title,
            message='Не дождались заголовка Дзена'
        )

    @allure.step('Проскролить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Подождать прогрузки нужного номера вопроса в аккордеоне "Вопросы о важном"')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важном"')
    def click_on_faq_items(self, data):
        self.click_on_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Подождать прогрузки нужного номера ответа в аккордеоне "Вопросы о важном"')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answers_items[data])

    @allure.step('Получить текст нужного номера ответа в аккордеоне "Вопросы о главном"')
    def get_displayed_text_from_faq_answer(self, data):
        return self.get_text_on_element(MainPageLocators.faq_answers_items[data])