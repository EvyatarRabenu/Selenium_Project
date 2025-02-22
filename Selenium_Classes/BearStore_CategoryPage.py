from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BearStoreCategoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def products_list(self):
        """Returns all <a> tags within the product div."""
        return self.driver.find_elements(By.CSS_SELECTOR, ".product-list-container > .artlist a span")


    def click_on_product(self, product_name):
        """ Clicks on the product with the given name. """
        for product in self.products_list():
            if product.text.strip() == product_name:
                product.click()
                return

    def get_header_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".h3")

