from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BearStoreSignInPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def start_register_button_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.register-button')

    def enter_username_log_in(self, user_name):
        user_name_field = self.driver.find_element(By.ID, 'UsernameOrEmail')
        user_name_field.clear()
        user_name_field.send_keys(user_name)

    def enter_email_log_in(self , email):
        email_field = self.driver.find_element(By.ID, 'UsernameOrEmail')
        email_field.clear()
        email_field.send_keys(email)

    def enter_password_log_in(self, password):
        password_field = self.driver.find_element(By.ID, 'Password')
        password_field.clear()
        password_field.send_keys(password)

    def login_button_element(self):
        return self.driver.find_element(By.CLASS_NAME , 'btn-login')





