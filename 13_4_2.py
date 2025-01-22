import openpyxl

# Creating a new Excel file
workbook = openpyxl.Workbook()
sheet = workbook.active

# Writing data to the file
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

# Saving the file
workbook.save('example.xlsx')
