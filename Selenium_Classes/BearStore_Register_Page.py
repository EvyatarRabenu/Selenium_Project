from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BearStoreRegisterPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver


    def enter_first_name(self, first_name):
        """ Finds the first name input field and enters the given first name. """
        first_name_field = self.driver.find_element(By.ID, 'FirstName')
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        """ Finds the last name input field and enters the given last name. """
        last_name_field = self.driver.find_element(By.ID, 'LastName')
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def select_birth_date(self, day, month, year):
        """ Selects the birthdate by choosing day, month, and year from dropdown menu. """
        day_dropdown = Select(self.driver.find_element(By.ID, "DateOfBirthDay"))
        day_dropdown.select_by_value(day)
        month_dropdown = Select(self.driver.find_element(By.ID, "DateOfBirthMonth"))
        month_dropdown.select_by_visible_text(month)
        year_dropdown = Select(self.driver.find_element(By.ID, "DateOfBirthYear"))
        year_dropdown.select_by_value(year)

    def enter_email(self, email):
        """ Finds the email input field and enters the given email address. """
        email_field = self.driver.find_element(By.ID, 'Email')
        email_field.clear()
        email_field.send_keys(email)

    def enter_username(self, user_name):
        """ Finds the username input field and enters the given username. """
        user_name_field = self.driver.find_element(By.ID, 'Username')
        user_name_field.clear()
        user_name_field.send_keys(user_name)

    def enter_password(self, password):
        """ Finds the password and confirm password fields and enters the given password."""
        password_field = self.driver.find_element(By.ID, 'Password')
        password_field.clear()
        password_field.send_keys(password)

        confirm_password_field = self.driver.find_element(By.ID, "ConfirmPassword")
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)

    def finish_register_button_element(self):
        """ Finds and returns the 'Registration' button element at the end of the registration process. """
        return self.driver.find_element(By.CLASS_NAME , 'btn-lg')

    def continue_button_element(self):
        """ Finds and returns the 'Continue' button element. """
        return self.driver.find_element(By.CLASS_NAME , 'btn-secondary')
