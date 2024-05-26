import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    @allure.step("Открыть страницу по URL")
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step("Скролл к элементу страницы")
    def execute_script(self, locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url
