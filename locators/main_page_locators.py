from selenium.webdriver.common.by import By


class MainPageLocators:
    main_header = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')
    questions_faq = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    }

    answers_faq = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }

    order_button_in_main = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button')
    order_button_in_header = (By.XPATH, '//button[@class = "Button_Button__ra12g"]')

    header_logo_scooter = (By.XPATH, '//a[@class = "Header_LogoScooter__3lsAR"]')
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru"]')
    title_of_page = (By.TAG_NAME, 'title')