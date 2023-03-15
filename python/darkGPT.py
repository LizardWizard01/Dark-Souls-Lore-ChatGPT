import openpyxl
from openpyxl import load_workbook
wb = openpyxl.load_workbook(filename='dsexcel.xlsx')
print(type(wb))
wb.sheetnames
print(wb.sheetnames)
sheet = wb['Items']
# I'm getting "list object is not callable" as an error here, and not sure what it is talking about.