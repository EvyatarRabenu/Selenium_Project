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

    def get_header_element(self):
        return self.driver.find_element(By.CSS_SELECTOR,'.pd-name')

    def get_price(self):
        price_strip = self.driver.find_element(By.CSS_SELECTOR, '.pd-price > span').text.strip()
        price_str = ''.join(char for char in price_strip if char.isdigit() or char == '.')
        price = float(price_str)
        return price

    def enter_quantity_product(self, quantity):
        """ Finding the quantity field and entering the desired number of units """
        quantity_field = self.driver.find_element(By.CSS_SELECTOR, ".form-control-lg")
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))
