from selenium.webdriver.common.by import By


class MainPageLocators:
    YANDEX_LOGO_IN_HEADER = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
    SCOOTER_LOGO_IN_HEADER = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]
    ORDER_BUTTON_IN_HEADER = [By.XPATH, ".//div[contains(@class, 'Header')]/button[text()='Заказать']"]
    ORDER_STATUS_BUTTON_IN_HEADER = [By.XPATH, ".//div[contains(@class, 'Header')]/button[text()='Статус заказа']"]
    ORDER_BUTTON_IN_MIDDLE = [By.XPATH, ".//div[contains(@class, 'Home')]/button[text()='Заказать']"]
    COOKIE_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    FAQ_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]


class AnswersQuestionsFAQ:
    # FIRST_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-0"]
    # FIRST_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__panel-0 > p"]
    # SECOND_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-1"]
    # SECOND_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__panel-1 > p"]
    # THIRD_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-2"]
    # THIRD_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__panel-2 > p"]
    # FOURTH_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-3"]
    # FOURTH_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__panel-3 > p"]
    # FIFTH_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-4"]
    # FIFTH_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__panel-4 > p"]
    # SIXTH_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-5"]
    # SIXTH_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__panel-5 > p"]
    # SEVENTH_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-6"]
    # SEVENTH_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__panel-6 > p"]
    # EIGHTH_QUESTION_BUTTON = [By.CSS_SELECTOR, "#accordion__heading-7"]
    # EIGHTH_QUESTION_ANSWER = [By.CSS_SELECTOR, "#accordion__heading-7 > p"]


    FIRST_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-0']"]
    FIRST_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-0']"]
    SECOND_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-1']"]
    SECOND_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-1']"]
    THIRD_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-2']"]
    THIRD_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-2']"]
    FOURTH_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-3']"]
    FOURTH_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-3']"]
    FIFTH_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-4']"]
    FIFTH_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-4']"]
    SIXTH_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-5']"]
    SIXTH_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-5']"]
    SEVENTH_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-6']"]
    SEVENTH_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-6']"]
    EIGHTH_QUESTION_BUTTON = [By.XPATH, "//*[@id='accordion__heading-7']"]
    EIGHTH_QUESTION_ANSWER = [By.XPATH, "//*[@id='accordion__panel-7']"]


class OrderPageLocators:
    FIRST_NAME = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    INCORRECT_FIRST_NAME_MESSAGE = [By.XPATH, "//div[text()='Введите корректное имя']"]
    LAST_NAME = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    INCORRECT_LAST_NAME_MESSAGE = [By.XPATH, "//div[text()='Введите корректную фамилию']"]
    ADDRESS_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    INCORRECT_ADDRESS_MESSAGE = [By.XPATH, "//div[text()='Введите корректный адрес']"]
    METRO_STATION_FIELD = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]
    INCORRECT_METRO_STATION_MESSAGE = [By.XPATH, "//div[text()='Выберите станцию']"]

    @staticmethod
    def METRO_STATION_HINT_BUTTON(station_name: str):
        return [By.XPATH, f".//div[text()='{station_name}']/parent::button"]

    TELEPHONE_NUMBER = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
    INCORRECT_TELEPHONE_NUMBER_MESSAGE = [By.XPATH, "//div[text()='Введите корректный номер']"]

    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    BACK_BUTTON = [By.XPATH, ".//button[text()='Назад']"]
    ABOUT_RENT_PAGE = [By.XPATH, ".//div[text()='Про аренду']"]
    DATE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    RENT_TIME_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    RENT_TIME_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHOISE = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    COMMENT_FOR_COURIER = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON_IN_ORDERING_FORM = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_COMPLETED_BANNER = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    SHOW_ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]
