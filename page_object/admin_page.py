import random

from page_object.base_page import Basepage
from selenium.webdriver.common.by import By
import time


class AdminPage(Basepage):
    CATALOG = (By.CSS_SELECTOR, ".fa.fa-tags.fw")
    PRODUCTS = (By.XPATH, ".//a[text()='Products']")
    ADD_BUTTON = (By.CSS_SELECTOR, ".fa.fa-plus")
    G = (By.CSS_SELECTOR, ".table tbody input")
    DEL_BUTTON = (By.CSS_SELECTOR, ".fa.fa-trash-o")

    def switch_to_product_page(self):
        self.element(self.CATALOG).click()
        self.element(self.PRODUCTS).click()
        self.element(self.ADD_BUTTON).click()

    def switch_to_product_page_catalog(self):
        self.element(self.CATALOG).click()
        self.element(self.PRODUCTS).click()

    def find_and_remove_product(self):
        list_all_items = self.find_elements(self.G)
        for index in range(len(list_all_items)):
            print(random.choice(list_all_items))
            break
        self.element(self.DEL_BUTTON).click()

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        time.sleep(2)
