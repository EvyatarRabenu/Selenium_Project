from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BearStoreProductPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def products_list(self):
        """ Returns all <a> tags within the product div."""
        return self.driver.find_elements(By.CSS_SELECTOR, ".artlist a span")

    def selected_product(self, product_name):
        """ Clicks on the product with the given name. """
        for product in self.products_list():
            if product.text.strip() == product_name:
                product.click()
                return




