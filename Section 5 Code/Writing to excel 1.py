from tkinter import ttk
from datetime import datetime
import tkinter as tk
import xlrd
from xlutils.copy import copy
import xlwt
from PIL import ImageTk, Image

# make the excel file to store information

style1 = xlwt.XFStyle()
style1.num_format_str = "D-MM-YY"
#
# wb = xlwt.Workbook()
# sheet1 = wb.add_sheet("May 2018", cell_overwrite_ok=True)
# sheet1.write(0, 0, datetime.now(), style1)
#
#
# wb.save("May 2018 orders.xls")

read_workbook = xlrd.open_workbook("May 2018 orders.xls", formatting_info=True)
read_sheet = read_workbook.sheet_by_index(0)

workbook = copy(read_workbook)
sheet = workbook.get_sheet(0)


sheet.write(0, 0, datetime.now(), style1)
sheet.write(0, 1, "Item")
sheet.write(0, 2, "Size")
sheet.write(0, 3, "Color")
sheet.write(0, 4, "Quantity")


number = read_sheet.nrows

print(number)

workbook.save("May 2018 orders.xls")


