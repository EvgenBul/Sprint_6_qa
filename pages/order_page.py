import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage



class OrderPage(BasePage):

    @allure.step('Кликнуть по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.metro_dropdown_list)

    @allure.step('Ввести дату заказа в поле "Когда привезти самокат"')
    def send_keys_date_by_keyboard_input(self, keys):
        self.send_keys_to_input(OrderPageLocators.input_date, keys)

    @allure.step('Кликнуть по выбранной дате в выпадающем календаре поля ввода даты начала аренды')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.calendar_item)

    @allure.step('Проверка наличия кнопки "Посмотреть статус" после создания заказа')
    def check_of_button_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.button_check_status_of_order)

    @allure.step('Заполнение первой части формы - "Для кого самокат"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.input_name)
        self.click_on_element(OrderPageLocators.input_name)
        self.send_keys_to_input(OrderPageLocators.input_name, test_data[0])
        self.click_on_element(OrderPageLocators.input_lastname)
        self.send_keys_to_input(OrderPageLocators.input_lastname, test_data[1])
        self.click_on_element(OrderPageLocators.input_address)
        self.send_keys_to_input(OrderPageLocators.input_address, test_data[2])
        self.click_on_element(OrderPageLocators.input_metro)
        self.send_keys_to_input(OrderPageLocators.input_metro, test_data[3])
        self.click_on_element(OrderPageLocators.metro_dropdown_list)
        self.click_on_element(OrderPageLocators.input_phone)
        self.send_keys_to_input(OrderPageLocators.input_phone, test_data[4])
        self.click_on_element(OrderPageLocators.button_further)

    @allure.step('Заполнение второй части формы - "Про аренду"')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.input_date)
        self.click_on_element(OrderPageLocators.input_date)
        self.send_keys_to_input(OrderPageLocators.input_date, test_data[5])
        self.click_on_element(OrderPageLocators.checkbox_grey_color_scooter)
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(OrderPageLocators.dropdown_item_rental_period)
        self.click_on_element(OrderPageLocators.input_comment)
        self.send_keys_to_input(OrderPageLocators.input_comment, test_data[6])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)