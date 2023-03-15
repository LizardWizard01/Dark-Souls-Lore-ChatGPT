import openpyxl
wb = openpyxl.load_workbook('dsexcel.xlsx')
type(wb)
wb.get_sheet_names()
sheet = wb['Items']
# I'm getting "list object is not callable" as an error here, and not sure what it is talking about.
tuple(sheet['A1':'M850'])
for cellObj in sheet.columns[5]:
    print(cellObj.value)
# We want columns B, E, and H
# print(tuple(sheet))
