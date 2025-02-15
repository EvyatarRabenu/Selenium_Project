from time import sleep

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BearStoreShoppingBasketPage:
    def __init__(self , driver : webdriver.Chrome):
        self.driver = driver

    def get_header_element(self):
        return self.driver.find_element(By.CLASS_NAME ,'h3')

    # def change_quantity_for_all_products(self, quantities):
    #     wait = WebDriverWait(self.driver, 20)  # המתנה של עד 10 שניות
    #     quantity_fields = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@data-step='1']")))
    #     # if len(quantity_fields) < len(quantities):
    #     #     print("Warning: Not all quantity fields were found!")
    #     for i in range(len(quantities)):
    #         quantity_field = wait.until(EC.element_to_be_clickable(quantity_fields[i]))  # להמתין שהשדה יהיה קליקבילי
    #         quantity_field.clear()
    #         quantity_field.send_keys(str(quantities[i]))
    #         wait = WebDriverWait(self.driver, 20)  # המתנה של עד 10 שניות
    #         print(f"Changed quantity for element {i} to {quantities[i]}")
    #     return quantities

    def change_quantity_for_all_products(self, quantities):
        wait = WebDriverWait(self.driver, 20)  # המתנה של עד 20 שניות
        quantity_fields = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@data-step='1']")))

        if len(quantity_fields) < len(quantities):
            print("Warning: Not all quantity fields were found!")

        for i in range(len(quantities)):
            quantity_field = wait.until(EC.element_to_be_clickable(quantity_fields[i]))  # להמתין שהשדה יהיה קליקבילי
            quantity_field.clear()
            quantity_field.send_keys(str(quantities[i]))
            print(f"Changed quantity for element {i} to {quantities[i]}")

            # המתנה שהטקסט יופיע בשדה הכמות
            wait.until(
                EC.text_to_be_present_in_element_value((By.XPATH, f"//input[@data-step='1']"), str(quantities[i])))

            # מציאת האלמנט של הדף ולחיצה עליו כדי לעדכן את הכמות
            page_element = self.driver.find_element(By.CSS_SELECTOR, '.h3')
            wait.until(EC.element_to_be_clickable(page_element)).click()
            print("Clicked on page element to update quantity")

            # המתנה נוספת לודא שהכמות עודכנה
            wait.until(
                EC.text_to_be_present_in_element_value((By.XPATH, f"//input[@data-step='1']"), str(quantities[i])))

        return quantities



    def price_list_elements(self):
        """ מחזירה רשימה של מחירי המוצרים בעגלת הקניות בפורמט מספרי בלבד """
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, ".cart-col-subtotal > span")
        price_list = []
        for price in price_elements:
            price_strip = price.text.strip()
            price = ''.join(char for char in price_strip if char.isdigit() or char == '.')
            price_list.append(float(price))
        return price_list

    # def price_list_elements(self):
    #     """ מחזירה רשימה של מחירי המוצרים בעגלת הקניות בפורמט מספרי בלבד, עם הדפסות לבדיקת נתונים """
    #     price_elements = self.driver.find_elements(By.CSS_SELECTOR, ".cart-col-subtotal > span")
    #
    #     print(f"🔎 Found {len(price_elements)} price elements.")  # הדפסה לבדיקה כמה מחירים נמצאו
    #
    #     price_list = []
    #
    #     for index, price in enumerate(price_elements):
    #         price_strip = price.text.strip()  # מחיקת רווחים מיותרים
    #         print(f"🛒 Raw text from element {index}: {price_strip}")  # הצגת הטקסט לפני עיבוד
    #
    #         price_clean = ''.join(
    #             char for char in price_strip if char.isdigit() or char == '.')  # שמירה רק על מספרים ונקודה
    #
    #         if price_clean:  # בדיקה שהתוצאה לא ריקה
    #             numeric_price = float(price_clean)
    #             print(f"✅ Extracted numeric price: {numeric_price}")  # הצגת המחיר לאחר עיבוד
    #             price_list.append(numeric_price)  # הוספת המחיר לרשימה
    #
    #     print(f"📋 Final price list: {price_list}")  # הצגת כל המחירים לאחר העיבוד
    #
    #     return price_list

    # def total_price_list_elements(self):
    #     wait = WebDriverWait(self.driver, 20)  # המתנה של עד 20 שניות להמתנה יותר ארוכה אם צריך
    #     total_price_elements = wait.until(
    #         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-caption='Total']>span.price")))
    #     total_price_list = []
    #     for price in total_price_elements:
    #         total_price_strip = price.text.strip()
    #         price = ''.join(char for char in total_price_strip if char.isdigit() or char == '.')
    #         total_price_list.append(float(price))
    #     return total_price_list


    def total_price_list_elements(self):
        """ מחזירה רשימה של מחירי ה-TOTAL בעגלת הקניות בפורמט מספרי בלבד """
        wait = WebDriverWait(self.driver, 20)  # המתנה של עד 20 שניות להמתנה יותר ארוכה אם צריך
        total_price_elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-caption='Total']>span.price")))
        # total_price_elements = self.driver.find_elements(By.XPATH, "//div[@data-caption='Total']/span[@class='price']")

        print(f"Number of total price elements found: {len(total_price_elements)}")

        total_price_list = []
        for index, price in enumerate(total_price_elements):
            total_price_strip = price.text.strip()
            print(f"Raw price text [{index}]: {total_price_strip}")  # הדפסה של הטקסט הגולמי

            price = ''.join(char for char in total_price_strip if char.isdigit() or char == '.')
            print(f"Extracted numeric price [{index}]: {price}")  # הדפסה אחרי שליפת המספרים

            total_price_list.append(float(price))
            sleep(2)  # השהיה קצרה בכל איטרציה בלולאה כדי לוודא שהמערכת תתעדכן כראוי

        print(f"Final extracted total prices list: {total_price_list}")  # הדפסה של הרשימה הסופית
        return total_price_list

    def checkout_button_element(self):
        return self.driver.find_element(By.ID , 'checkout')

    def remove_all_products(self):
        """ Recursively removes all products from the shopping basket by clicking
        the delete button and waiting for each item to be removed before proceeding."""
        delete_button_list = self.driver.find_elements(By.CSS_SELECTOR, '.btn-gray')

        if not delete_button_list:  # Base case: stop if no buttons are found
            return

        delete_button_list[0].click()  # Remove the first product
        WebDriverWait(self.driver, 5).until(EC.staleness_of(delete_button_list[0]))  # Wait until it's removed
        # Recursive call to remove the next product with the updated list
        self.remove_all_products()

