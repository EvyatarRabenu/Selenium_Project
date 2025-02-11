from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BearStoreAddToCart2:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver


    def select_product(self, product_name):
        """ Selects a certain product and adds it to the cart with a certain amount """
        products = self.driver.find_elements(By.CSS_SELECTOR, ".artlist a span")
        for product in products:
            if product.text.strip() == product_name:
                product.click()
                break

    def enter_quantity_product1(self, quantity):
        """ Finding the quantity field and entering the desired number of units """
        quantity_field = self.driver.find_element(By.CSS_SELECTOR, ".form-control-lg")
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

    def enter_quantity_product2(self, quantity):
        """ Finding the quantity field and entering the desired number of units """
        quantity_field = self.driver.find_element(By.CSS_SELECTOR, ".form-control-lg")
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

    def click_add_to_basket(self):
        """ Finding the "Add to Cart" button and clicking it """
        add_to_basket_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-block")
        add_to_basket_btn.click()

    def get_cart_quantity(self):
        """ Returns the total amount of products in the basket """
        quantities = self.driver.find_elements(By.XPATH,"//div[@class='offcanvas-cart-item']//input[@name='item.EnteredQuantity']")
        total_quantity = 0

        for quantity in quantities:
            total_quantity += int(quantity.get_attribute("value"))

        return total_quantity