🐻 BearStore Selenium Tests
Automated UI tests for the BearStore demo shopping site, built with Python and Selenium using the unittest framework.

🎯 What’s Tested?
Browsing categories & products

Adding/removing items from the shopping basket

User registration, login & logout

Checkout flow and order confirmation

Basket quantities and price validations

📂 Project Structure
Selenium_Classes/ — Page Objects for site interactions

Selemium_Tests/data_from_excel.py — Excel read/write utilities

test_bearstore.py — Main test cases

test_data.xlsx — Test inputs and results

⚙️ Setup & Run
Install dependencies:

bash
Copy
Edit
pip install selenium openpyxl
Make sure Chrome and matching ChromeDriver are installed and in your PATH.

Close test_data.xlsx before running tests.

Run all tests:

bash
Copy
Edit
python -m unittest test_bearstore.py
📝 Notes
Test data is read from and results are saved to the Excel file

Uses explicit waits for stable UI testing

Tests cover key user flows and basket behaviors
