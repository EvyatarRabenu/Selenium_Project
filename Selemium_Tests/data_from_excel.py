import openpyxl

def read_category_from_excel(file_path):
    """Reads the category name from the specified xlsx file."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    category_name = sheet["A1"].value.strip()  # Ensure it removes extra spaces in the Excel file
    workbook.close()
    return category_name

def write_test_result_to_excel(file_path, cell, result):
    """Writes the test result (e.g., 'Pass' or 'Fail') to the specified cell in the xlsx file."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    sheet[cell] = result  # Write the test result to the specified cell
    workbook.save(file_path)  # Save the changes
    workbook.close()

def read_product_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    product_name = sheet["A2"].value.strip()  # Ensure it removes extra spaces in the Excel file
    workbook.close()
    return product_name

def read_home_page_title_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    home_page_title = sheet["A4"].value.strip()  # Ensure it removes extra spaces in the Excel file
    workbook.close()
    return home_page_title