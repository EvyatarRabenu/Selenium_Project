from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BearStoreHomePage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def categories_list(self):
        """Returns all <a> tags within the category div."""
        return self.driver.find_elements(By.CSS_SELECTOR, ".artlist-homepage-categories a span")

    def selected_category(self, category_name):
        """ Clicks on the category with the given name. """
        for category in self.categories_list():
            if category.text.strip() == category_name:
                category.click()
                return




