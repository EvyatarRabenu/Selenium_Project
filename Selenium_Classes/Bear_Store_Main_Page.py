from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BearStoreHomePage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def categories_list(self):
        """Returns all <a> tags within the category div , Give 12 Links of the categories"""
        return self.driver.find_elements(By.CSS_SELECTOR, ".artlist-homepage-categories a span")

    def selected_category(self, category_name):
        """ Clicks on the category with the given name. """
        for category in self.categories_list():
            if category.text.strip() == category_name:
                category.click()
                return

    def return_to_home_page(self):
        """ Clicks the element to return to the home page. """
        self.driver.find_element(By.CLASS_NAME,'brand').click()


    def get_shopping_basket_element(self):
        """ Returns the shopping basket element """
        return self.driver.find_element(By.CSS_SELECTOR , '#shopbar-cart>a')
