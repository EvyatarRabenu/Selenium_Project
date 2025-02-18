from unittest import TestCase
import logging
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium_Classes.BearStore_Main_Page import BearStoreHomePage
from selenium.webdriver.common.by import By
from Selemium_Tests.data_from_excel import *
from Selenium_Classes.BearStore_Product_Page import BearStoreProductPage
from Selenium_Classes.BearStore_Shopping_Basket_Side_Bar import BearStoreSideBarBasket
from Selenium_Classes.BaerStore_Shopping_Basket_Page import BearStoreShoppingBasketPage
from Selenium_Classes.BearStore_Register_Page import BearStoreRegisterPage
from Selenium_Classes.BearStore_Sign_In_Page import BearStoreSignInPage
from Selenium_Classes.BearStore_CheckOut import BearStoreCheckOut



class TestPageTransitions(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bearstore-testsite.smartbear.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home_page = BearStoreHomePage(self.driver)
        self.product_page = BearStoreProductPage(self.driver)
        self.basket_side_bar = BearStoreSideBarBasket(self.driver)
        self.shopping_basket_page = BearStoreShoppingBasketPage(self.driver)
        self.register_page = BearStoreRegisterPage(self.driver)
        self.sign_in_page = BearStoreSignInPage(self.driver)
        self.checkout = BearStoreCheckOut(self.driver)

    def test_page_transition_and_header_verification(self):
        # Read test data from the Excel file
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"
        category_name = read_data_from_excel(file_path , 'N2')
        product_name = read_data_from_excel(file_path , 'N4')
        home_page_title_name = read_data_from_excel(file_path , 'O40')

        # Use HomePage class to select the category
        self.home_page.selected_category(category_name)

        # Verify that the page header matches the selected category
        header_element = self.driver.find_element(By.CSS_SELECTOR, ".h3")
        self.assertEqual(category_name.lower(), header_element.text.strip().lower())


        # -------------------------------------- End of section a1 -------------------------------------------------------------
        # -------------------------------------- Strat of section a2 -----------------------------------------------------------

        # Second Test (Product) - Run this regardless of the first test result
        # Use ProductPage class to select the product
        self.product_page.selected_product(product_name)

        # Verify that the page header matches the selected product
        header_element = self.driver.find_element(By.CSS_SELECTOR, '.pd-name')
        self.assertEqual(product_name.lower(), header_element.text.strip().lower())

        # -------------------------------------- End of section a2 -------------------------------------------------------------
        # -------------------------------------- Strat of section a3 -----------------------------------------------------------

        self.driver.back()
        # wait until previous page loads
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        header_element = self.driver.find_element(By.CSS_SELECTOR, ".h3")
        self.assertEqual(category_name.lower(), header_element.text.strip().lower())

        # --------------------------------------- End of section a3 ------------------------------------------------------------
        # ---------------------------------------Start of section a4 -----------------------------------------------------------

        self.driver.back()
        # wait until previous page loads
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        home_page_title = self.driver.find_element(By.CSS_SELECTOR, ".h2")
        self.assertEqual(home_page_title_name.lower(), home_page_title.text.strip().lower())
        write_test_result_to_excel(file_path, "N21", "V")

        # ------------------------------------ End of Test 1 -----------------------------------------------------------
        # ---------------------------------- Start of Test 2 -----------------------------------------------------------

    def test_add_two_products_and_verify_basket_quantity(self):
        # Read test data from the Excel file
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"

        category_name1 = read_data_from_excel(file_path , 'M2')
        product_name1 = read_data_from_excel(file_path, 'M4')
        quantity_product1 = read_data_from_excel(file_path, 'M5')

        category_name2 = read_data_from_excel(file_path, 'M7')
        product_name2 = read_data_from_excel(file_path, 'M9')
        quantity_product2 = read_data_from_excel(file_path , 'M10')

        # Select first product and add to the basket
        self.home_page.selected_category(category_name1)
        self.product_page.selected_product(product_name1)
        self.product_page.enter_quantity_product(quantity_product1)
        self.basket_side_bar.click_add_to_basket()

        # Navigate back to home page and select second product
        self.home_page.return_to_home_page_element().click()
        self.home_page.selected_category(category_name2)
        self.product_page.selected_product(product_name2)
        self.product_page.enter_quantity_product(quantity_product2)
        self.basket_side_bar.click_add_to_basket()

        # Wait until product quantities are updated in the shopping basket
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='offcanvas-cart-item']//input[@name='item.EnteredQuantity']")))

        # Verify that the total quantity in the basket is correct
        total_quantity = self.basket_side_bar.get_cart_quantity_sum()
        self.assertEqual(total_quantity, (int(quantity_product1) + int(quantity_product2)))

        # Write test result to the Excel file and clean up by removing all products
        write_test_result_to_excel(file_path, "M21", "V")
        self.basket_side_bar.remove_all_products()

    # ----------------------------------------------- Start of Test 3 --------------------------------------------------

    def test_add_three_products_and_verify_basket_details(self):
        # Read category, product names, and quantities from the Excel file.
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

        # Add the first product to the basket.
        self.home_page.selected_category(category_name1)
        WebDriverWait(self.driver , 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h3")))
        self.product_page.selected_product(product_name1)
        product_name1 = self.product_page.get_header_element().text
        product_price1 = self.product_page.get_price()
        quantity_product1 = self.product_page.enter_quantity_product(quantity_product1)
        self.basket_side_bar.click_add_to_basket()
        # Back to Home Page
        self.home_page.whole_page_element().click()
        self.home_page.return_to_home_page_element().click()


        # Add the second product to the basket.
        self.home_page.selected_category(category_name2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h3")))
        self.product_page.selected_product(product_name2)
        product_name2 = self.product_page.get_header_element().text
        product_price2 = self.product_page.get_price()
        quantity_product2 = self.product_page.enter_quantity_product(quantity_product2)
        self.basket_side_bar.click_add_to_basket()
        # Back to Home Page
        self.home_page.whole_page_element().click()
        self.home_page.return_to_home_page_element().click()


        # Add the third product to the basket.
        self.home_page.selected_category(category_name3)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h3")))
        self.product_page.selected_product(product_name3)
        product_name3 = self.product_page.get_header_element().text
        product_price3 = self.product_page.get_price()
        quantity_product3 = self.product_page.enter_quantity_product(quantity_product3)
        self.basket_side_bar.click_add_to_basket()

        # Get product details from the basket and compare with the selected products.
        basket_page_product1_name = self.basket_side_bar.products_name_list_elements()[2].text #Opposite location
        basket_page_product2_name = self.basket_side_bar.products_name_list_elements()[1].text #Opposite location
        basket_page_product3_name = self.basket_side_bar.products_name_list_elements()[0].text #Opposite location

        basket_page_product1_price = self.basket_side_bar.price_list_elements()[2] #Opposite location
        basket_page_product2_price = self.basket_side_bar.price_list_elements()[1] #Opposite location
        basket_page_product3_price = self.basket_side_bar.price_list_elements()[0] #Opposite location

        basket_page_product1_quantity = self.basket_side_bar.get_quantity_list()[2] #Opposite location
        basket_page_product2_quantity = self.basket_side_bar.get_quantity_list()[1] #Opposite location
        basket_page_product3_quantity = self.basket_side_bar.get_quantity_list()[0] #Opposite location

        # Verify that the product names, prices, and quantities match.
        self.assertEqual(product_name1 , basket_page_product1_name)
        self.assertEqual(product_name2 , basket_page_product2_name)
        self.assertEqual(product_name3 , basket_page_product3_name)

        self.assertEqual(product_price1 , basket_page_product1_price)
        self.assertEqual(product_price2 , basket_page_product2_price)
        self.assertEqual(product_price3 , basket_page_product3_price)

        self.assertEqual(int(quantity_product1) , basket_page_product1_quantity)
        self.assertEqual(int(quantity_product2) , basket_page_product2_quantity)
        self.assertEqual(int(quantity_product3) , basket_page_product3_quantity)


        # Write the test result to the Excel file and remove all products from the basket.
        write_test_result_to_excel(file_path, "L21", "V")
        self.basket_side_bar.remove_all_products()

        # ---------------------------------------- Start of Test 4 -----------------------------------------------------

    def test_delete_one_product_from_basket(self):
        # Read test data from the Excel file
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"

        category_name1 = read_data_from_excel(file_path ,'K2')
        product_name1 = read_data_from_excel(file_path ,'K4')
        category_name2 = read_data_from_excel(file_path , 'K7')
        product_name2 = read_data_from_excel(file_path , 'K9')

        # Select and add the first product to the basket.
        self.home_page.selected_category(category_name1)
        self.product_page.selected_product(product_name1)
        product_price1 = self.product_page.get_price()
        product_name1 = self.product_page.get_header_element().text
        self.basket_side_bar.click_add_to_basket()

        # Return to the homepage and select another category and product.
        self.home_page.return_to_home_page_element().click()
        self.home_page.selected_category(category_name2)
        self.product_page.selected_product(product_name2)

        # Remove the first product from the basket and wait until the removal is complete.
        self.basket_side_bar.click_add_to_basket()
        initial_count = len(self.basket_side_bar.products_name_list_elements())
        self.basket_side_bar.remove_product_by_index(0)
        WebDriverWait(self.driver, 10).until(lambda driver: len(self.basket_side_bar.products_name_list_elements()) == initial_count - 1)

        # Verify that the correct product remains in the basket with the correct price and quantity.
        self.assertEqual(product_name1, self.basket_side_bar.products_name_list_elements()[0].text)
        self.assertEqual(product_price1, self.basket_side_bar.price_list_elements()[0])
        self.assertEqual(1, self.basket_side_bar.get_quantity_list()[0])


        write_test_result_to_excel(file_path, "K21", "V")
        self.basket_side_bar.remove_all_products()

    # ---------------------------------------- Start of Test 5 ---------------------------------------------------------
    def test_add_to_basket_and_verify_transitions(self):
        # Read test data from the Excel file
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"

        category_name1 = read_data_from_excel(file_path ,'J2')
        product_name1 = read_data_from_excel(file_path ,'J4')
        shopping_cart_page_title = read_data_from_excel(file_path , 'O36')

        # Select category, product, and add product to the basket.
        self.home_page.selected_category(category_name1)
        self.product_page.selected_product(product_name1)
        self.basket_side_bar.click_add_to_basket()

        # Wait until the basket's header element is visible and verify it.
        subtotal_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".offcanvas-cart-header")))
        self.assertTrue(subtotal_element.is_displayed())

        # ------------------------------------- Start of Section 2 -----------------------------------------------------

        # Close the basket side pop up by clicking in the middle of the page and wait for it to disappear.
        self.driver.find_element(By.CLASS_NAME , 'canvas-blocker').click()
        # Wait until the cart popup disappears
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".offcanvas-cart-header")))
        # Verify that the cart is no longer visible
        self.assertFalse(self.basket_side_bar.is_cart_visible())

        # ------------------------------------- Start of Section 3 -----------------------------------------------------

        # Open the shopping basket and verify it's visible.
        self.home_page.shopping_basket_element().click()
        # Verify that the basket is visible
        self.assertTrue(self.basket_side_bar.is_cart_visible())

        # ------------------------------------- Start of Section 4 -----------------------------------------------------

        # Wait for the "Go to Cart" button to be visible, click it, and verify the shopping cart page title.
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-success")))
        self.basket_side_bar.go_to_cart_button().click()
        self.assertEqual(shopping_cart_page_title , self.shopping_basket_page.get_header_element().text)

        # Write the test result to the Excel file and remove all products from the basket.
        write_test_result_to_excel(file_path , "J21", "V")
        self.home_page.return_to_home_page_element().click()
        self.home_page.shopping_basket_element().click()
        self.basket_side_bar.remove_all_products()

    # ------------------------------------------- Start of Test 6 ------------------------------------------------------

    def test_shopping_basket_total_matches_expected_price(self):
        # Read category, product names, and quantities from the Excel file.
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"

        category_name1 = read_data_from_excel(file_path , 'I2')
        product_name1 = read_data_from_excel(file_path, 'I4')
        quantity_product1 = read_data_from_excel(file_path , 'I5')

        category_name2 = read_data_from_excel(file_path, 'I7')
        product_name2 = read_data_from_excel(file_path, 'I9')
        quantity_product2 = read_data_from_excel(file_path, 'I10')

        category_name3 = read_data_from_excel(file_path ,'I11')
        product_name3 = read_data_from_excel(file_path , 'I13')
        quantity_product3 = read_data_from_excel(file_path, 'I14')

        # Select and add the first product to the basket
        self.home_page.selected_category(category_name1)
        self.product_page.selected_product(product_name1)
        product1_price = self.product_page.get_price()
        self.product_page.enter_quantity_product(quantity_product1)
        self.basket_side_bar.click_add_to_basket()
        self.home_page.return_to_home_page_element().click()

        # Select and add the second product to the basket
        self.home_page.selected_category(category_name2)
        self.product_page.selected_product(product_name2)
        product2_price = self.product_page.get_price()
        self.product_page.enter_quantity_product(quantity_product2)
        self.basket_side_bar.click_add_to_basket()
        self.home_page.return_to_home_page_element().click()

        # Select and add the third product to the basket
        self.home_page.selected_category(category_name3)
        self.product_page.selected_product(product_name3)
        product3_price = self.product_page.get_price()
        self.product_page.enter_quantity_product(quantity_product3)
        self.basket_side_bar.click_add_to_basket()

        # Get the total price displayed in the basket sidebar
        basket_side_bar_total_price = self.basket_side_bar.get_total_amount_price()

        # Calculate the expected total price
        total_price = ((product1_price * int(quantity_product1)) +
                       (product2_price * int(quantity_product2)) +
                       (product3_price * int(quantity_product3)))

        # Added log prints before testing to see the calculations
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        logging.info(f"Product 1 - Name: {product_name1}, Price: {product1_price}, Quantity: {quantity_product1}")
        logging.info(f"Product 2 - Name: {product_name2}, Price: {product2_price}, Quantity: {quantity_product2}")
        logging.info(f"Product 3 - Name: {product_name3}, Price: {product3_price}, Quantity: {quantity_product3}")
        logging.info(f"Calculated total price: {total_price}")
        logging.info(f"Basket sidebar total price: {basket_side_bar_total_price}")

        self.assertEqual(basket_side_bar_total_price , total_price)

        # Navigate to the cart, verify the total price, write the test result to the Excel file, and clear the basket.
        self.basket_side_bar.go_to_cart_button()
        basket_side_bar_total_price = self.basket_side_bar.get_total_amount_price()
        self.assertEqual(basket_side_bar_total_price , total_price)
        write_test_result_to_excel(file_path , "I21", "V")
        self.basket_side_bar.remove_all_products()

    # --------------------------------------------- Strat of Test 7 ----------------------------------------------------

    def test_add_products_update_quantities_and_check_totals(self):
        # Read category, product names, and quantities from the Excel file.
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"

        category_name1 = read_data_from_excel(file_path , 'H2')
        product_name1 = read_data_from_excel(file_path, 'H4')
        quantity_product1 = read_data_from_excel(file_path , 'H5')

        category_name2 = read_data_from_excel(file_path, 'H7')
        product_name2 = read_data_from_excel(file_path, 'H9')
        quantity_product2 = read_data_from_excel(file_path, 'H10')

        quantity_list = [quantity_product2, quantity_product1]

        # Select and add the first product to the basket
        self.home_page.selected_category(category_name1)
        self.product_page.selected_product(product_name1)
        product1_price = self.product_page.get_price()
        self.basket_side_bar.click_add_to_basket()
        self.home_page.return_to_home_page_element().click()

        # Select and add the second product to the basket
        self.home_page.selected_category(category_name2)
        self.product_page.selected_product(product_name2)
        product2_price = self.product_page.get_price()
        self.basket_side_bar.click_add_to_basket()

        # Wait for the "Go to Cart" button to be visible and click it
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-success")))
        self.basket_side_bar.go_to_cart_button().click()

        # Change quantities and wait for the updates
        self.shopping_basket_page.change_quantities(quantity_list)

        # Fetch updated unit prices from the cart
        unit_price_list = self.shopping_basket_page.get_unit_price_list()[::-1]

        # Calculate expected prices using the updated unit prices
        expected_price1 = unit_price_list[0] * float(quantity_product1)
        expected_price2 = unit_price_list[1] * float(quantity_product2)

        # Verify the updated total prices
        total_products_price_list = self.shopping_basket_page.get_total_products_price_list()[::-1]

        self.assertAlmostEqual(total_products_price_list[0], expected_price1)
        self.assertAlmostEqual(total_products_price_list[1], expected_price2)

        # Verify the subtotal
        sub_total = (float(self.shopping_basket_page.get_total_products_price_list()[0]) +
                     float(self.shopping_basket_page.get_total_products_price_list()[1]))

        self.assertEqual(self.shopping_basket_page.get_sub_total_price(), sub_total)

        # Clean up: Remove all products from the cart
        write_test_result_to_excel(file_path , "H21", "V")
        #self.basket_side_bar.remove_all_products()
        self.shopping_basket_page.remove_all_products()

       # ------------------------------------------- Start of Test 8 ---------------------------------------------------

    def test_full_checkout_process_with_two_items(self):
        # Read test data from an Excel file
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"

        # Read category and product names
        category_name1 = read_data_from_excel(file_path , 'G2')
        product_name1 = read_data_from_excel(file_path, 'G4')
        category_name2 = read_data_from_excel(file_path, 'G7')
        product_name2 = read_data_from_excel(file_path, 'G9')

        # Read registration data
        first_name = read_data_from_excel(file_path , 'O23')
        last_name = read_data_from_excel(file_path , 'N23')
        day = read_data_from_excel(file_path , 'M24')
        month = read_data_from_excel(file_path ,'L24')
        year = read_data_from_excel(file_path ,'K24')
        email = read_data_from_excel(file_path , 'J23')
        user_name = read_data_from_excel(file_path , 'I23')
        password = read_data_from_excel(file_path , 'H23')
        confirm_password = read_data_from_excel(file_path ,'G23')

        # Check if an account was already created
        is_account_created = read_data_from_excel(file_path , 'E25')

        # Read expected confirmation message after order completion
        confirmation_msg = read_data_from_excel(file_path , 'O33')

        # Read expected message when shopping basket is empty
        empty_shopping_basket = read_data_from_excel(file_path , 'O34')


        # Read login data
        user_name_log_in = read_data_from_excel(file_path , 'N15')
        email_log_in = read_data_from_excel(file_path , 'N17')
        password_log_in = read_data_from_excel(file_path , 'N19')

        # Read billing address data
        first_name_billing_address = read_data_from_excel(file_path , 'O25')
        last_name_billing_address = read_data_from_excel(file_path , 'N25')
        email_billing_address = read_data_from_excel(file_path , 'J25')


        # Select and add the first product to the basket
        self.home_page.selected_category(category_name1)
        self.product_page.selected_product(product_name1)
        self.basket_side_bar.click_add_to_basket()
        self.home_page.whole_page_element().click()
        self.home_page.return_to_home_page_element().click()

        # Select and add the second product to the basket
        self.home_page.selected_category(category_name2)
        self.product_page.selected_product(product_name2)
        self.basket_side_bar.click_add_to_basket()

        # Wait for the "Checkout" button to be visible and click it
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-clear")))
        self.basket_side_bar.checkout_button_element().click()

        # Handle login or new user registration
        if is_account_created == 'Positive':
            # If the account exists, log in
            self.sign_in_page.enter_username_log_in(user_name_log_in)
            self.sign_in_page.enter_password_log_in(password_log_in)
            self.sign_in_page.login_button_element().click()
            self.shopping_basket_page.checkout_button_element().click()


        else:
            # If the account does not exist, register a new user
            self.sign_in_page.start_register_button_element().click()
            self.register_page.enter_first_name(first_name)
            self.register_page.enter_last_name(last_name)
            self.register_page.select_birth_date(day,month,year)
            self.register_page.enter_email(email)
            self.register_page.enter_username(user_name)
            self.register_page.enter_password(password)
            self.register_page.enter_password(confirm_password)
            self.register_page.finish_register_button_element().click()
            self.register_page.continue_button_element().click()

            # Mark account as created in the Excel file
            write_test_result_to_excel(file_path , 'E25' , 'Positive')

        # Step 6: Complete the checkout process
        self.checkout.enter_first_name(first_name_billing_address)
        self.checkout.enter_last_name(last_name_billing_address)
        self.checkout.enter_email(email_billing_address)
        self.checkout.next_button_billing_address_element().click()
        self.checkout.ship_to_this_address_button_element().click()
        self.checkout.next_button_shipping_method_element().click()
        self.checkout.next_button_payment_method_element().click()
        self.checkout.agree_to_terms_checkbox().click()
        self.checkout.confirm_button_element().click()

        # Verify order confirmation message
        self.assertEqual(confirmation_msg.strip() , self.checkout.header_order_received_msg_element().text.strip())

        # Verify order number correctly
        order_number = self.checkout.order_number_element().text
        self.checkout.order_details_button_element().click()
        self.assertEqual(order_number.strip(), self.checkout.order_details_element().text.strip())

        # Verify shopping basket is empty after checkout
        self.home_page.shopping_basket_element().click()
        self.assertEqual(empty_shopping_basket.strip() , self.basket_side_bar.empty_cart_header().text.strip())

        # Write test result to the Excel file
        write_test_result_to_excel(file_path , "G21", "V")

    # ----------------------------------------- Start of Test 9 --------------------------------------------------------

    def test_user_can_login_and_logout(self):
        # Read test data from the Excel file
        file_path = r"C:\Users\EvyatarRabenu\Desktop\test_data.xlsx"
        user_name_log_in = read_data_from_excel(file_path , 'N15')
        password_log_in = read_data_from_excel(file_path , 'N19')
        log_in_name_header_from_excel = read_data_from_excel(file_path , 'O44')

        # Perform login
        self.home_page.login_element().click()
        self.sign_in_page.enter_username_log_in(user_name_log_in)
        self.sign_in_page.enter_password_log_in(password_log_in)
        self.sign_in_page.login_button_element().click()

        # Verify successful login by checking the displayed username
        self.assertEqual(user_name_log_in.strip().lower() , self.home_page.login_element_user_logged_in().text.strip().lower())

        # Perform logout
        self.home_page.login_element().click()
        self.home_page.logout_element().click()

        # Verify successful logout by checking the displayed login text
        self.assertEqual(log_in_name_header_from_excel.strip().lower() , self.home_page.login_element().text.strip().lower())

        # Write test result to the Excel file
        write_test_result_to_excel(file_path, 'F21', 'V')


    def tearDown(self):
        sleep(6)
        self.driver.quit()