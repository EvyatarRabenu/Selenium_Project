from time import sleep

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BearStoreShoppingBasketPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def get_header_element(self):
        return self.driver.find_element(By.CLASS_NAME ,'h3')




    def change_quantity_for_all_products(self, quantities):
        wait = WebDriverWait(self.driver, 10)  # המתנה של עד 10 שניות
        #product_elements = self.driver.find_elements(By.XPATH, "//input[contains(@class,'itemquantity')]")
        product_elements = self.driver.find_elements(By.XPATH, "//input[@data-step='1']")
        print(f"Found {len(product_elements)} quantity fields.")
        for i in range(len(quantities)):
            print(f"Changing quantity for element {i} to {quantities[i]}")
            quantity_field = wait.until(EC.element_to_be_clickable(product_elements[i]))
            quantity_field.clear()
            quantity_field.send_keys(quantities[i])
            sleep(1)  # השהיה של שניה אחת

        return quantities



    def remove_all_products(self):
        """ Recursively removes all products from the shopping basket by clicking
        the delete button and waiting for each item to be removed before proceeding."""
        delete_button_list = self.driver.find_elements(By.CSS_SELECTOR, '.btn-gray')

        if not delete_button_list:  # Base case: stop if no buttons are found
            return

        delete_button_list[0].click()  # Remove the first product
        WebDriverWait(self.driver, 5).until(EC.staleness_of(delete_button_list[0]))  # Wait until it's removed
        # Recursive call to remove the next product with the updated list
        self.remove_all_products()

