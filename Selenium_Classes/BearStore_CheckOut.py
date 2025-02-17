from selenium import  webdriver
from selenium.webdriver.common.by import By


class BearStoreCheckOut:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def enter_first_name(self , first_name):
        """ Enters the first name in the billing address form """
        first_name_field = self.driver.find_element(By.ID , 'NewAddress_FirstName')
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        """ Enters the last name in the billing address form """
        last_name_field = self.driver.find_element(By.ID, 'NewAddress_LastName')
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_email(self, email):
        """ Enters the email in the billing address form """
        email_field = self.driver.find_element(By.ID, 'NewAddress_Email')
        email_field.clear()
        email_field.send_keys(email)

    def next_button_billing_address_element(self):
        """ Returns the 'Next' button element for the billing address step. """
        return self.driver.find_element(By.CLASS_NAME , 'new-address-next-step-button')

    def ship_to_this_address_button_element(self):
        """ Returns the 'Ship to this address' button element. """
        return self.driver.find_element(By.CLASS_NAME , 'select-shipping-address-button')

    def next_button_shipping_method_element(self):
        return self.driver.find_element(By.CLASS_NAME , 'shipping-method-next-step-button')

    def next_button_payment_method_element(self):
        return self.driver.find_element(By.CLASS_NAME , 'btn-warning')

    def agree_to_terms_checkbox(self):
        return self.driver.find_element(By.ID , 'termsofservice')

    def confirm_button_element(self):
        return self.driver.find_element(By.CLASS_NAME , 'btn-danger')

    def header_order_received_msg_element(self):
        return self.driver.find_element(By.TAG_NAME , 'h1')

    def order_details_button_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.btn-warning')

    def order_number_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'p > a > strong')

    def order_details_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "small[class='text-muted']>small")