from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BearStoreProductPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def products_list(self):
        """ Returns all <a> tags within the product div."""
        return self.driver.find_elements(By.CSS_SELECTOR, ".artlist a span")


    def get_header_element(self):
        """ Returns the product name header element """
        return self.driver.find_element(By.CSS_SELECTOR,'.pd-name')

    def get_price(self):
        """ Retrieves the product price, extracts only numerical values, and converts it to a float.
        return: Product price as a float. """
        price_strip = self.driver.find_element(By.CSS_SELECTOR, '.pd-price > span').text.strip()
        price_str = ''.join(char for char in price_strip if char.isdigit() or char == '.')
        price = float(price_str)
        return price

    def get_quantity_product(self, quantity):
        """ Finding the quantity field and entering the desired number of units """
        quantity_field = self.driver.find_element(By.CSS_SELECTOR, ".form-control-lg")
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))
        return quantity
