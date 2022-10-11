from page_object.base_page import Basepage
from selenium.webdriver.common.by import By


class ProductPage(Basepage):
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    DESCRIPTION = (By.CLASS_NAME, "note-editable")
    BUTTON_SAVE = (By.CSS_SELECTOR, ".fa.fa-save")
    TAB_DATA = (By.XPATH, ".//*[@class='nav nav-tabs']/li/a[text()='Data']")
    MODEL = (By.ID, "input-model")

    def adding_new_item(self, product_name, meta_tag_title, description, model):
        self._input(self.PRODUCT_NAME, product_name)
        self._input(self.META_TAG_TITLE, meta_tag_title)
        self._input(self.DESCRIPTION, description)
        self.click(self.TAB_DATA)
        self._input(self.MODEL, model)
        self.click(self.BUTTON_SAVE)
