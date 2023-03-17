import openpyxl
from openpyxl import load_workbook
wb = openpyxl.load_workbook('dsDesc.xlsx')
type(wb)
sheet = wb.get_sheet_by_name('Items')
#tuple(sheet['A1':'M850'])
#for cellObj in sheet.columns[E]:
#    print(cellObj.value)




