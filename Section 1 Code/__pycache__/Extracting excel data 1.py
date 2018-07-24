import xlrd as xl

workbook = xl.open_workbook("outstanding_balances.xlsx")

sheet = workbook.sheet_by_name("Sheet1")

#row, col
# print(sheet.cell(0, 1).value)
#
# print(sheet.nrows)
#
# print(sheet.ncols)

# for col in range(sheet.ncols):
#     print(sheet.cell_value(1, col))

#start
names = sheet.col_values(0, 1, sheet.nrows)
print(names)

# start col, start row, range
outstanding = sheet.col_values(2, 1, sheet.nrows)
print(outstanding)

emails = sheet.col_values(1, 1, sheet.nrows)
print(emails)






