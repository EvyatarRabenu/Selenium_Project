from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BearStoreShoppingBasketPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def get_header_element(self):
        return self.driver.find_element(By.CLASS_NAME ,'h3')

