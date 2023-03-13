import openpyxl
wb = openpyxl.load_workbook('dsexcel.xlsx')
type(wb)
wb.sheetnames()
sheet = wb['Items']
# I'm getting "list object is not callable" as an error here, and not sure what it is talking about.