from openpyxl import load_workbook

# Load the workbook
workbook = load_workbook("merged_data.xlsx")

# Count the number of worksheets
worksheet_count = len(workbook.worksheets)
print("Number of worksheets:", worksheet_count)
