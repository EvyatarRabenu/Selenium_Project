import openpyxl

def read_data_from_excel(file_path , cell):
    """Reads the category name from the specified excel file."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = str(sheet[cell].value).strip()  # Ensure it removes extra spaces in the Excel file
    workbook.close()
    return data

def write_test_result_to_excel(file_path, cell, result):
    """ Writes the test result (if its Pass or not) to the specified cell in the excel file."""
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    sheet[cell] = result  # Write the test result to the specified cell
    workbook.save(file_path)  # Save the changes
    workbook.close()


