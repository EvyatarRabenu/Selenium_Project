from itertools import product
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
from Selenium_Classes.Bear_Store_Shopping_Basket import BearStoreAddToCart2


class TestPageTransitions(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bearstore-testsite.smartbear.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home_page = BearStoreHomePage(self.driver)
        self.product_page = BearStoreProductPage(self.driver)
        self.basket_page = BearStoreAddToCart2(self.driver)

    def test_page_transition(self):
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"
        category_name = read_data_from_excel(file_path , 'N2')
        product_name = read_data_from_excel(file_path , 'N4')
        home_page_title_name = read_data_from_excel(file_path , 'N6')


        # Use HomePage class to select the category
        self.home_page.selected_category(category_name)

        # Verify that the page header matches the selected category
        header_element = self.driver.find_element(By.CSS_SELECTOR, ".h3")
        self.assertEqual(category_name.lower(), header_element.text.strip().lower())

        # Write "V" to cell N18 if the test passes
        write_test_result_to_excel(file_path, "N19", "V")

        # -------------------------------------- End of a1 -------------------------------------------------------------
        # -------------------------------------- Strat of a2 -----------------------------------------------------------

        # Second Test (Product) - Run this regardless of the first test result
        # Use ProductPage class to select the product
        self.product_page.selected_product(product_name)

        # Verify that the page header matches the selected product
        header_element = self.driver.find_element(By.CSS_SELECTOR, '.pd-name')
        self.assertEqual(product_name.lower(), header_element.text.strip().lower())

        # Write "Pass" to cell B2 if the test passes
        #write_test_result_to_excel(file_path, "M18", "V")

        # -------------------------------------- End of a2 -------------------------------------------------------------
        # -------------------------------------- Strat of a3 -----------------------------------------------------------

        self.driver.back()
        # wait until previous page loads
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        header_element = self.driver.find_element(By.CSS_SELECTOR, ".h3")
        self.assertEqual(category_name.lower(), header_element.text.strip().lower())
        #write_test_result_to_excel(file_path, "L18", "V")

        # --------------------------------------- End of a3 ------------------------------------------------------------
        # ---------------------------------------Start of a4 -----------------------------------------------------------

        self.driver.back()
        # wait until previous page loads
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        home_page_title = self.driver.find_element(By.CSS_SELECTOR, ".h2")
        self.assertEqual(home_page_title_name.lower(), home_page_title.text.strip().lower())
        write_test_result_to_excel(file_path, "N19", "V")

        # ------------------------------------ End of part 1 -----------------------------------------------------------
        # ---------------------------------- Start of part 2 -----------------------------------------------------------

    def test_add_to_basket_two_products(self):
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"

        category_name1 = read_data_from_excel(file_path , 'M2')
        product_name1 = read_data_from_excel(file_path, 'M4')
        quantity_product1 = read_data_from_excel(file_path, 'M5')

        category_name2 = read_data_from_excel(file_path, 'M7')
        product_name2 = read_data_from_excel(file_path, 'M9')
        quantity_product2 = read_data_from_excel(file_path , 'M10')

        # Choose Category #1
        self.home_page.selected_category(category_name1)


        # Choose Product #1
        self.product_page.selected_product(product_name1)
        self.product_page.enter_quantity_product(quantity_product1)
        self.basket_page.click_add_to_basket()

        # Back to Home Page And choose Category #2
        self.home_page.return_to_home_page()
        self.home_page.selected_category(category_name2)


        # Choose Product #2
        self.product_page.selected_product(product_name2)
        self.product_page.enter_quantity_product(quantity_product2)
        self.basket_page.click_add_to_basket()


        # Compare sum of the two products to total amount
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='offcanvas-cart-item']//input[@name='item.EnteredQuantity']")))
        total_quantity = self.basket_page.get_cart_quantity_sum()

        print(f"Total quantity in basket: {total_quantity}")
        self.assertEqual(total_quantity, (int(quantity_product1) + int(quantity_product2)))
        write_test_result_to_excel(file_path, "M19", "V")
        self.basket_page.remove_all_products()


    # ----------------------------------------------- Start of part 3 --------------------------------------------------

    def test_add_to_basket_three_products_and_compare(self):
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"
        category_name1 = read_data_from_excel(file_path , 'L2')
        product_name1 = read_data_from_excel(file_path, 'L4')
        quantity_product1 = read_data_from_excel(file_path , 'L5')

        category_name2 = read_data_from_excel(file_path, 'L7')
        product_name2 = read_data_from_excel(file_path, 'L9')
        quantity_product2 = read_data_from_excel(file_path, 'L10')

        category_name3 = read_data_from_excel(file_path ,'L11')
        product_name3 = read_data_from_excel(file_path , 'L13')
        quantity_product3 = read_data_from_excel(file_path, 'L14')


        # Choose Category #1
        self.home_page.selected_category(category_name1)
        WebDriverWait(self.driver , 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h3")))
        # Choose Product #1
        self.product_page.selected_product(product_name1)
        product_name1 = self.product_page.get_header_element().text
        product_price1 = self.product_page.get_price()
        quantity_product1 = self.product_page.enter_quantity_product(quantity_product1)
        self.basket_page.click_add_to_basket()
        # Back to Home Page
        self.home_page.return_to_home_page()


        # Choose Category #2
        self.home_page.selected_category(category_name2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h3")))
        # Choose Product #2
        self.product_page.selected_product(product_name2)
        product_name2 = self.product_page.get_header_element().text
        product_price2 = self.product_page.get_price()
        quantity_product2 = self.product_page.enter_quantity_product(quantity_product2)
        self.basket_page.click_add_to_basket()
        # Back to Home Page
        self.home_page.return_to_home_page()


        # Choose Category # 3
        self.home_page.selected_category(category_name3)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h3")))
        # Choose Product #3
        self.product_page.selected_product(product_name3)
        product_name3 = self.product_page.get_header_element().text
        product_price3 = self.product_page.get_price()
        quantity_product3 = self.product_page.enter_quantity_product(quantity_product3)
        self.basket_page.click_add_to_basket()

        basket_page_product1_name = self.basket_page.products_name_list_elements()[2].text #Opposite loaction
        basket_page_product2_name = self.basket_page.products_name_list_elements()[1].text #Opposite loaction
        basket_page_product3_name = self.basket_page.products_name_list_elements()[0].text #Opposite loaction

        basket_page_product1_price = self.basket_page.price_list_elements()[2]
        basket_page_product2_price = self.basket_page.price_list_elements()[1]
        basket_page_product3_price = self.basket_page.price_list_elements()[0]

        basket_page_product1_quantity = self.basket_page.get_quantity_list()[2]
        basket_page_product2_quantity = self.basket_page.get_quantity_list()[1]
        basket_page_product3_quantity = self.basket_page.get_quantity_list()[0]

        self.assertEqual(product_name1 , basket_page_product1_name)
        self.assertEqual(product_name2 , basket_page_product2_name)
        self.assertEqual(product_name3 , basket_page_product3_name)

        self.assertEqual(product_price1 , basket_page_product1_price)
        self.assertEqual(product_price2 , basket_page_product2_price)
        self.assertEqual(product_price3 , basket_page_product3_price)

        self.assertEqual(int(quantity_product1) , basket_page_product1_quantity)
        self.assertEqual(int(quantity_product2) , basket_page_product2_quantity)
        self.assertEqual(int(quantity_product3) , basket_page_product3_quantity)

        write_test_result_to_excel(file_path, "L19", "V")
        self.basket_page.remove_all_products()

        #test 4

    def test_delete_one_product_from_basket(self):
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"
        category_name1 = read_data_from_excel(file_path ,'K2')
        product_name1 = read_data_from_excel(file_path ,'K4')
        category_name2 = read_data_from_excel(file_path , 'K7')
        product_name2 = read_data_from_excel(file_path , 'K9')

        self.home_page.selected_category(category_name1)
        self.product_page.selected_product(product_name1)

        product_price1 = self.product_page.get_price()
        product_name1 = self.product_page.get_header_element().text
        self.basket_page.click_add_to_basket()
        # Back to Home Page
        self.home_page.return_to_home_page()


        self.home_page.selected_category(category_name2)
        self.product_page.selected_product(product_name2)


        self.basket_page.click_add_to_basket()
        initial_count = len(self.basket_page.products_name_list_elements())
        self.basket_page.remove_product_by_index(0)
        WebDriverWait(self.driver, 10).until(lambda driver: len(self.basket_page.products_name_list_elements()) == initial_count -1)
        self.assertEqual(product_name1 , self.basket_page.products_name_list_elements()[0].text)
        self.assertEqual(product_price1 , self.basket_page.price_list_elements()[0])
        self.assertEqual(1 , self.basket_page.get_quantity_list()[0])

        write_test_result_to_excel(file_path, "K19", "V")
        self.basket_page.remove_all_products()




    def tearDown(self):
        sleep(2)
        self.driver.quit()