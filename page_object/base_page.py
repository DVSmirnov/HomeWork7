from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {path}')
    def open(self, path):
        try:
            self.driver.logger.info("Opening url: {}".format(self.driver.base_url + path))
            self.driver.get(self.driver.base_url + path)
        except Exception:
            self.driver.logger.error(f'Error during opening url {self.driver.base_url + path}')
            allure.attach(self.driver.get_screenchot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Страница {self.driver.base_url + path} не открывается"

    @allure.step('Кликнуть на локатор {locator}')
    def click(self, locator):
        try:
            self.driver.logger.info("Clicking element: {}".format(locator))
            ActionChains(self.driver).move_to_element(self.element(locator=locator)).pause(0.1).click().perform()
        except Exception:
            self.driver.logger.error(f'Error during clicking in {locator}')
            allure.attach(self.driver.get_screenchot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Не удалось кликнуть на локатор {locator}"

    @allure.step('Ввести значение {value} в локатор {locator}')
    def _input(self, locator, value):
        try:
            self.driver.logger.info("Input {} in input {}".format(value, locator))
            web_element = self.element(locator=locator)
            self.click(locator=locator)
            web_element.clear()
            web_element.send_keys(value)
        except Exception:
            self.driver.logger.error(f'Error during entering {value} in {locator}')
            allure.attach(self.driver.get_screenchot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Не удалось ввести значение {value} в локатор {locator}"

    @allure.step('Проверка наличия локатора {locator}')
    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenchot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Ожидание локатора {locator} заняло слишком много времени"

    @allure.step('Проверка наличия локаторов {locator}')
    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenchot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Ожидание локатора {locator} заняло слишком много времени"

    @allure.step('Проверить, что элемент {product_name} присутствует в локаторе {locator}')
    def product_name_varified(self, product_name, locator):
        self.driver.logger.info("Check if element {} is present".format(locator))
        return self.element((By.LINK_TEXT, product_name))

    @allure.step('Найти все элементы с локатором {locator}')
    def find_elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenchot_as_png(), 'Screenshot', attachment_type=allure.attachment_type.PNG)
            assert False, f"Ожидание локатора {locator} заняло слишком много времени"
