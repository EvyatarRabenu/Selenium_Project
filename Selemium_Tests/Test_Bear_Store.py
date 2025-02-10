from unittest import TestCase
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium_Classes.Bear_Store_Main_Page import BearStoreHomePage
from selenium.webdriver.common.by import By
from Selemium_Tests.data_from_excel import *
from Selenium_Classes.Bear_Store_Product_Page import BearStoreProductPage


class TestPageTransitions(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bearstore-testsite.smartbear.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home_page = BearStoreHomePage(self.driver)
        self.product_page = BearStoreProductPage(self.driver)

    def test_page_transition(self):
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"
        category_name = read_category_from_excel(file_path)
        product_name = read_product_from_excel(file_path)
        home_page_title_name = read_home_page_title_from_excel(file_path)


        # Use HomePage class to select the category
        self.home_page.selected_category(category_name)

        # Verify that the page header matches the selected category
        header_element = self.driver.find_element(By.CSS_SELECTOR, ".h3")
        self.assertEqual(category_name.lower(), header_element.text.strip().lower())

        # Write "Pass" to cell B1 if the test passes
        write_test_result_to_excel(file_path, "B1", "Pass")

        # ---------------------------------- End of 1a -------------------------------------------

        # Second Test (Product) - Run this regardless of the first test result
        # Use ProductPage class to select the product
        self.product_page.selected_product(product_name)

        # Verify that the page header matches the selected product
        header_element = self.driver.find_element(By.CSS_SELECTOR, '.pd-name')
        self.assertEqual(product_name.lower(), header_element.text.strip().lower())

        # Write "Pass" to cell B2 if the test passes
        write_test_result_to_excel(file_path, "B2", "Pass")

        # -------------------------------------- End of a2 ---------------------------------------------------

        self.driver.back()
        # wait until previous page loads
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        header_element = self.driver.find_element(By.CSS_SELECTOR, ".h3")
        self.assertEqual(category_name.lower(), header_element.text.strip().lower())
        write_test_result_to_excel(file_path, "B3", "Pass")

        # --------------------------------------- End of a3 ----------------------------------------------------

        self.driver.back()
        # wait until previous page loads
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        home_page_title = self.driver.find_element(By.CSS_SELECTOR, ".h2")
        self.assertEqual(home_page_title_name.lower(), home_page_title.text.strip().lower())
        write_test_result_to_excel(file_path, "B4", "Pass")



    def tearDown(self):
        sleep(2)
        self.driver.quit()