import allure

from main_data.locators import OrderPageLocators
from pages.base_page import BasePage


class YandexScooterOrderPage(BasePage):

    @allure.step("Ввод имени")
    def input_first_name(self, first_name: str):
        return self.find_element(OrderPageLocators.FIRST_NAME).send_keys(first_name)

    @allure.step("Ввод фамилии")
    def input_last_name(self, last_name: str):
        return self.find_element(OrderPageLocators.LAST_NAME).send_keys(last_name)

    @allure.step("Ввод адреса")
    def input_address(self, address: str):
        return self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step("Выбор метро")
    def choose_subway(self, subway_name: str):
        self.find_element(OrderPageLocators.METRO_STATION_FIELD).click()
        return self.find_element(OrderPageLocators.METRO_STATION_HINT_BUTTON(subway_name)).click()

    @allure.step("Ввод номера телефона")
    def input_telephone_number(self, telephone_number: str):
        return self.find_element(OrderPageLocators.TELEPHONE_NUMBER).send_keys(telephone_number)

    @allure.step("Заполнить данные на шаге 'Для кого самокат'")
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.input_telephone_number(data_set['tel_number'])

    @allure.step("Заполнение некорректных данных на шаге 'Для кого самокат'")
    def fill_user_uncorrect_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.input_telephone_number(data_set['tel_number'])

    @allure.step("Заполнить данные на этапе 'Про аренду'")
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        for option in data_set['color']:
            self.choose_color(option)
        self.input_comment(data_set['comment_for_courier'])

    @allure.step("Перейти на следующий этап заказа")
    def go_next(self):
        return self.find_element(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step("Ввод даты")
    def input_date(self, date: str):
        return self.find_element(OrderPageLocators.DATE_FIELD).send_keys(date)

    @allure.step("Выбор периода аренды")
    def choose_rental_period(self, option: int):
        self.find_element(OrderPageLocators.RENT_TIME_FIELD).click()
        return self.find_elements(OrderPageLocators.RENT_TIME_LIST)[option].click()

    @allure.step("Выбор цвета")
    def choose_color(self, option: int):
        return self.find_elements(OrderPageLocators.COLOR_CHOISE)[option].click()

    @allure.step("Комментарий для курьера")
    def input_comment(self, comment_text):
        return self.find_element(OrderPageLocators.COMMENT_FOR_COURIER).send_keys(comment_text)

    @allure.step("Нажать 'Заказать'")
    def click_order(self):
        return self.find_element(OrderPageLocators.ORDER_BUTTON_IN_ORDERING_FORM).click()

    @allure.step("Подтвердить заказ")
    def click_accept_order(self):
        return self.find_element(OrderPageLocators.ACCEPT_ORDER_BUTTON).click()

    @allure.step("Перейти к статусу заказа")
    def click_go_to_status(self):
        return self.find_element(OrderPageLocators.SHOW_ORDER_STATUS_BUTTON).click()
