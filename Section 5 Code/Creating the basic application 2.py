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


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Ordering app")


        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Chair):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        item_label = tk.Label(self, text="Select your item ")
        item_label.grid(column=3, row=0)

        chair_button1 = tk.Button(self, text="Chair")

        chair_button1.grid(column=2, row=2)

        table_button = tk.Button(self, text="Table")

        table_button.grid(column=4, row=2)


        self.image = Image.open("furniture.jpg")
        self.image.thumbnail((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(self.image)
        label = tk.Label(image=photo)
        label.image = photo
        label.pack(side="left")

class Chair(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


app = App()
app.geometry("500x500")
app.mainloop()