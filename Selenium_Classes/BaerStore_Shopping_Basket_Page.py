from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BearStoreShoppingBasketPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def get_header_element(self):
        """ Returns the main header element of the page. """
        return self.driver.find_element(By.CLASS_NAME ,'h3')

    def get_total_amount_price(self):
        """ Retrieves and returns the total price of all items in the cart as a float. """
        price_strip = self.driver.find_element(By.CSS_SELECTOR,'.cart-summary-total >.cart-summary-value > span').text.strip()
        price_str = ''.join(char for char in price_strip if char.isdigit() or char == '.')
        price = float(price_str)
        return price

    def get_quantity_elements_list(self):
        """ Returns a list of input fields for item quantities in the cart.
         return List of elements representing quantity input fields. """
        return self.driver.find_elements(By.XPATH, "//div[@class='qty-input']//input")

    def change_quantities(self, quantity_list: list):
        """ Updates item quantities in the cart based on the
        provided list and waits for the price to update accordingly. """
        for i in range(len(quantity_list)):
            quantity_elements_list = self.get_quantity_elements_list()
            # Get the current price before changing the quantity
            initial_price = self.get_total_products_price_list()[i]

            quantity_elements_list[i].clear()
            quantity_elements_list[i].send_keys(quantity_list[i])
            quantity_elements_list[i].send_keys(Keys.TAB)

            # Wait for the total price to change from its initial value
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.get_total_products_price_list()[i] != initial_price)

    def get_total_products_price_list(self):
        """ Returns a list of prices for each product in the cart after processing the data.
        return List of product prices as float values. """
        price_elements_list = self.driver.find_elements(By.CSS_SELECTOR, '.cart-col-subtotal > span')
        price_list = []
        for price_element in price_elements_list:
            price_strip = price_element.text.strip()
            price = ''.join(char for char in price_strip if char.isdigit() or char == '.')
            price_list.append(float(price))
        return price_list

    def get_sub_total_price(self):
        """ Retrieves the subtotal price of the cart
        return Subtotal price as a float."""
        price_strip = self.driver.find_element(By.CSS_SELECTOR,
                                               'tr[class="cart-summary-total"]>td[class="cart-summary-value"] >span').text.strip()
        price_str = ''.join(char for char in price_strip if char.isdigit() or char == '.')
        price = float(price_str)
        return price

    def get_unit_price_list(self):
        """ Retrieves the list of unit prices for all products in the cart."""
        price_elements_list = self.driver.find_elements(By.CSS_SELECTOR, "div[data-caption='Price']>span.price")
        price_list = []
        for price_element in price_elements_list:
            price_strip = price_element.text.strip()
            price = ''.join(char for char in price_strip if char.isdigit() or char == '.')
            price_list.append(float(price))
        return price_list


    def checkout_button_element(self):
        """ Finds and returns the 'Checkout' button element. """
        return self.driver.find_element(By.ID , 'checkout')


    def remove_all_products(self):
        """ Removes all products from the shopping basket one by one using recursion,
         waiting for each item to be removed before continuing. """
        delete_button_list = self.driver.find_elements(By.CSS_SELECTOR, '.btn-gray')

        if not delete_button_list:  # Base case: stop if no buttons are found
            return

        delete_button_list[0].click()  # Remove the first product
        WebDriverWait(self.driver, 5).until(EC.staleness_of(delete_button_list[0]))  # Wait until it's removed
        # Recursive call to remove the next product with the updated list
        self.remove_all_products()

