from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


    def click_add_to_basket(self):
        """ Finding the "Add to Cart" button and clicking it """
        add_to_basket_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-block")
        add_to_basket_btn.click()

    def get_cart_quantity_sum(self):
        """ Returns the total amount of products in the basket """
        quantities = self.driver.find_elements(By.XPATH,"//div[@class='offcanvas-cart-item']//input[@name='item.EnteredQuantity']")
        total_quantity = 0
        for quantity in quantities:
            total_quantity += int(quantity.get_attribute("value"))
        return total_quantity

    def get_quantity_list(self):
        """ Returns the total amount of products in the basket """
        quantities = self.driver.find_elements(By.XPATH,"//div[@class='offcanvas-cart-item']//input[@name='item.EnteredQuantity']")
        quantity_list = []
        for quantity in quantities:
            quantity_list.append(int(quantity.get_attribute("value")))
        return quantity_list

    def remove_all_products(self):
        delete_button_list = self.driver.find_elements(By.CSS_SELECTOR, '.btn-to-danger')

        if not delete_button_list:  # Base case: stop if no buttons are found
            return

        delete_button_list[0].click()  # Remove the first product
        WebDriverWait(self.driver, 5).until(EC.staleness_of(delete_button_list[0]))  # Wait until it's removed
        # Recursive call to remove the next product with the updated list
        self.remove_all_products()

    def remove_product_by_index(self, index):
        delete_button_list = self.driver.find_elements(By.CSS_SELECTOR, '.btn-to-danger')
        if index >= len(delete_button_list) or index < 0:  # Check for valid index
            raise IndexError(f"Index {index} is out of range. Available products: {len(delete_button_list)}")
        delete_button_list[index].click()  # Remove the selected product



    def products_name_list_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.col-data >a')


    def price_list_elements(self):
        price_elements_list = self.driver.find_elements(By.CSS_SELECTOR , '.unit-price')
        price_list = []
        for price in price_elements_list:
            price_strip = price.text.strip()
            price = ''.join(char for char in price_strip if char.isdigit() or char == '.')
            price_list.append(float(price))
        return price_list

