from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BearStoreHomePage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver


    def categories(self):
        """ Return Category of some product """
        return self.driver.find_elements(By.LINK_TEXT , 'Show products in category Basketball')
