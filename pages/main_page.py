from pages.base_page import BasePage
import allure
from main_data.locators import MainPageLocators
from main_data.locators import YandexDzenLocators


class YandexScooterMainPage(BasePage):

    @allure.step("Нажать на кнопку заказа в хедере главной страницы")
    def click_order_button_in_header(self):
        return self.find_element(MainPageLocators.ORDER_BUTTON_IN_HEADER).click()

    @allure.step("Нажать на кнопку заказа в блоке 'Как это работает'")
    def click_order_button_in_middle(self):
        return self.find_element(MainPageLocators.ORDER_BUTTON_IN_MIDDLE).click()

    @allure.step("Нажать на вопрос в FAQ")
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(MainPageLocators.FAQ_BUTTONS, 10)
        return elems[question_number].click()

    @allure.step("Принять куки")
    def click_cookie_accept_button(self):
        return self.find_element(MainPageLocators.COOKIE_BUTTON).click()

    @allure.step("Возвращаем значение ответа от требуемого вопроса")
    def click_main_page_FAQ(self, button, answer):
        required_field = self.find_element(button)
        self.execute_script(required_field)
        self.find_element(button)
        required_field.click()
        return self.find_element(answer).text

    @allure.step("Перейти на страницу яндекса")
    def click_yandex_button(self):
        return self.find_element(MainPageLocators.YANDEX_LOGO_IN_HEADER).click()

    @allure.step("Перейти на главную страницу самоката")
    def click_scooter_button(self):
        return self.find_element(MainPageLocators.SCOOTER_LOGO_IN_HEADER).click()

    @allure.step("Переключение на вкладку браузера")
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step("Ожидание загрузки страницы 'Дзен'")
    def implicitly_wait_in_dzen(self):
        return self.find_element(YandexDzenLocators.DZEN_BLOCK).is_displayed()

    @allure.step("Найти блок с темами на странице 'Дзен'")
    def load_dzen_page(self):
        return self.find_element(YandexDzenLocators.DZEN_BLOCK).text
