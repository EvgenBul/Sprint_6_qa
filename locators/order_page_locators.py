from selenium.webdriver.common.by import By


class OrderPageLocators:
    button_yes_confirm_order = (By.XPATH, "//button[text()='Да']")
    button_check_status_of_order = (By.XPATH, ".//*[text()='Посмотреть статус']")

    input_name = (By.XPATH, "//input[@placeholder='* Имя']")
    input_lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    input_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    input_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro_dropdown_list = (By.XPATH, ".//li[@class='select-search__row']")
    input_phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_further = (By.XPATH, "//button[text()='Далее']")

    input_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, "//div[@class='react-datepicker-popper']")
    calendar_item = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    field_rental_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    dropdown_item_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    checkbox_grey_color_scooter = (By.XPATH, "//input[@id='grey']")
    input_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_make_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")