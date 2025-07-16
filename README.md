🐻 BearStore Selenium Test Project

This project automates UI testing for the BearStore demo shopping site using Python and Selenium, with unittest framework for solid test coverage.

🛒 Project Overview

* Navigate categories and select products
* Add, update, and remove items in the shopping basket
* User registration, login, and logout flows
* Complete checkout and order confirmation process
* Validate basket quantities and total prices

📂 Project Structure

* Selenium_Classes/ — Page Object classes for UI interaction
* Selemium_Tests/data_from_excel.py — Excel read/write helpers
* test_bearstore.py — Main unittest test cases
* test_data.xlsx — Excel file with input data and test results

🧪 Features

* Clear separation of UI logic and test logic
* Extensive unittest coverage for core user flows
* Tests driven by dynamic Excel input data
* Writes test pass/fail status back to Excel
* Uses explicit waits for stable Selenium automation


🚀 How to Run the Tests

Make sure you have Python installed. Then, from the project root directory, run:

```bash
python -m unittest test_bearstore.py

