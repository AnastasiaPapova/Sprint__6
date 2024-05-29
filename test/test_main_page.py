import allure
from main_data.all_urls import Urls
from pages.main_page import YandexScooterMainPage
from conftest import driver


class TestYandexScooterMainPage:

    @allure.title("Нажатие кнопки 'Заказать' в header на главной странице.")
    @allure.description("Проверка что, на главной странице в header по кнопке 'Заказать', просходит переход "
                        "на страницу 'Оформления заказа'.")
    def test_click_order_button_in_header_show_order_page(self, driver):
        yandex_scooter_main_page = YandexScooterMainPage(driver)
        yandex_scooter_main_page.go_to_site(Urls.MAIN_PAGE)
        yandex_scooter_main_page.click_cookie_accept_button()
        yandex_scooter_main_page.click_order_button_in_header()
        assert yandex_scooter_main_page.current_url() == Urls.ORDER_PAGE

    @allure.title("Нажатие кнопки 'Заказать' в блоке 'Как это работает' на главной странице.")
    @allure.description("Проверка что, на главной странице в блоке 'Как это работает' по кнопке 'Заказать', "
                        "просходит переход на страницу 'Оформления заказа'.")
    def test_click_order_button_in_middle_show_order_page(self, driver):
        yandex_scooter_main_page = YandexScooterMainPage(driver)
        yandex_scooter_main_page.go_to_site(Urls.MAIN_PAGE)
        yandex_scooter_main_page.click_cookie_accept_button()
        yandex_scooter_main_page.click_order_button_in_middle()

        assert yandex_scooter_main_page.current_url() == Urls.ORDER_PAGE

    @allure.title("Нажатие на лого 'Яндекс' в header на главной странице.")
    @allure.description("Проверка что, на главной странице в header по клику на лого 'Яндекс'происходит корреткный "
                        "редирект на страницу 'ЯндексДзен'.")
    def test_click_yandex_button_go_to_yandex(self, driver):
        yandex_scooter_main_page = YandexScooterMainPage(driver)
        yandex_scooter_main_page.go_to_site(Urls.MAIN_PAGE)
        yandex_scooter_main_page.click_cookie_accept_button()
        yandex_scooter_main_page.click_yandex_button()
        yandex_scooter_main_page.switch_window(1)
        yandex_scooter_main_page.wait_url_until_not_about_blank()
        yandex_scooter_main_page.implicitly_wait_in_dzen()
        check_dzen_block = yandex_scooter_main_page.load_dzen_page()

        assert check_dzen_block == 'Темы в Дзене'

    @allure.title("Нажатие на лого 'Самокат' в header на главной странице.")
    @allure.description("Проверка что, клик по логотипу 'Самокат' редиректит на главную 'Самокат' из страницы заказов.")
    def test_click_scooter_logo_go_to_scooter_main_page(self, driver):
        yandex_scooter_main_page = YandexScooterMainPage(driver)
        yandex_scooter_main_page.go_to_site(Urls.MAIN_PAGE)
        yandex_scooter_main_page.click_cookie_accept_button()
        yandex_scooter_main_page.click_order_button_in_header()
        yandex_scooter_main_page.click_scooter_button()
        current_url = yandex_scooter_main_page.current_url()

        assert current_url == Urls.MAIN_PAGE
