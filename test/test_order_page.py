import allure
import pytest
from pages.order_page import YandexScooterOrderPage
from pages.main_page import YandexScooterMainPage
from main_data.all_urls import Urls
from main_data.test_data import UserData
from main_data.locators import OrderPageLocators
from conftest import driver


class TestYandexScooterOrderPage:

    @allure.description("Проверка создания заказа по клику на кнопку 'Заказать' в хедере главной страницы ")
    @pytest.mark.parametrize('data_set', ['test_set1', 'test_set2'])
    def test_header_button_create_order_input_correct_data_and_show_order_banner(self, driver, data_set):
        order_page = YandexScooterOrderPage(driver)
        # order_page.go_to_site(Urls.ORDER_PAGE)
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Urls.MAIN_PAGE)
        main_page.click_cookie_accept_button()
        main_page.click_order_button_in_header()
        order_page.fill_user_data(UserData.test_data_sets[data_set])
        order_page.go_next()
        order_page.fill_rent_data(UserData.test_data_sets[data_set])
        order_page.click_order()
        order_page.click_accept_order()
        assert order_page.find_element(OrderPageLocators.ORDER_COMPLETED_BANNER).is_displayed()

    @allure.description("Проверка создания заказа по клику на кнопку 'Заказать' в блоке 'Как это работает' на"
                        " главной странице ")
    @pytest.mark.parametrize('data_set', ['test_set1', 'test_set2'])
    def test_middle_button_create_order_input_correct_data_and_show_order_banner(self, driver, data_set):
        order_page = YandexScooterOrderPage(driver)
        # order_page.go_to_site(Urls.ORDER_PAGE)
        main_page = YandexScooterMainPage(driver)
        main_page.go_to_site(Urls.MAIN_PAGE)
        main_page.click_cookie_accept_button()
        main_page.click_order_button_in_middle()
        order_page.fill_user_data(UserData.test_data_sets[data_set])
        order_page.go_next()
        order_page.fill_rent_data(UserData.test_data_sets[data_set])
        order_page.click_order()
        order_page.click_accept_order()
        assert order_page.find_element(OrderPageLocators.ORDER_COMPLETED_BANNER).is_displayed()

    @allure.description('Проверка что при корректных заполненных данных на этапе "Для кого самокат", '
                        'нажатии "Далее" происходит переход на следующий этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        order_page = YandexScooterOrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        main_page = YandexScooterMainPage(driver)
        main_page.click_cookie_accept_button()
        order_page.fill_user_data(UserData.test_data_sets['test_set1'])
        order_page.go_next()
        assert order_page.find_element(OrderPageLocators.ABOUT_RENT_PAGE).is_displayed()

    @allure.description("Проверка что при вводе некорректного имени, фамилии, номера телефона и адреса в форме "
                        "оформления заказа, выводится ошибка")
    def test_order_page_input_incorrect_data_show_error_message(self, driver):
        order_page = YandexScooterOrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        main_page = YandexScooterMainPage(driver)
        main_page.click_cookie_accept_button()
        order_page.fill_user_uncorrect_data(UserData.test_data_sets['incorrect_test_set'])
        order_page.go_next()
        assert order_page.find_element(OrderPageLocators.INCORRECT_FIRST_NAME_MESSAGE).is_displayed()
        assert order_page.find_element(OrderPageLocators.INCORRECT_LAST_NAME_MESSAGE).is_displayed()
        assert order_page.find_element(OrderPageLocators.INCORRECT_ADDRESS_MESSAGE).is_displayed()
        assert order_page.find_element(OrderPageLocators.INCORRECT_TELEPHONE_NUMBER_MESSAGE).is_displayed()

    @allure.description("Проверка что при пустом поле 'Метро' в форме оформление заказа, выводится ошибка")
    def test_order_page_metro_station_input_is_empty_show_error_message(self, driver):
        order_page = YandexScooterOrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        main_page = YandexScooterMainPage(driver)
        main_page.click_cookie_accept_button()
        order_page.go_next()
        assert main_page.find_element(OrderPageLocators.INCORRECT_METRO_STATION_MESSAGE).is_displayed()
