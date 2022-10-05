from page_object.base_page import Basepage
from selenium.webdriver.common.by import By


class CurrencyPage(Basepage):
    CURRENCY = (By.ID, 'form-currency')
    EURO = (By.NAME, 'EUR')
    POUND_STERLING = (By.NAME, 'GBP')
    US_DOLLAR = (By.NAME, 'USD')

    def switch_to_euro(self):
        self.element(self.CURRENCY).click()
        self.element(self.EURO).click()

    def switch_to_pound(self):
        self.element(self.CURRENCY).click()
        self.element(self.POUND_STERLING).click()

    def switch_to_dollar(self):
        self.element(self.CURRENCY).click()
        self.element(self.US_DOLLAR).click()
