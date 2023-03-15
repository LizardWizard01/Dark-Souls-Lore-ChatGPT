import openpyxl
from openpyxl import load_workbook
wb = openpyxl.load_workbook(filename='dsexcel.xlsx')
print(type(wb))
wb.sheetnames
print(wb.sheetnames)
sheet = wb['Items']
sheet[]
# I'm getting "list object is not callable" as an error here, and not sure what it is talking about.
# ebb: You needed to import what I added in line 2: the load_workbook. 