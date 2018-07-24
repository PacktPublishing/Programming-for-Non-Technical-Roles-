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

        for F in (StartPage, Chair, Table):
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

        chair_button1 = tk.Button(self, text="Chair",
                                  command=lambda: controller.show_frame(Chair))
        chair_button1.pack()
        chair_button1.grid(column=2, row=2)

        table_button = tk.Button(self, text="Table",
                                 command= lambda: controller.show_frame(Table))

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

        size_label = tk.Label(self, text="Enter the size")

        size_label.grid(column=0, row=0)
        self.size_entry = tk.Entry(self)
        self.size_entry.grid(column=2, row=0)

        color_label = tk.Label(self, text="Enter the color")
        color_label.grid(column=0, row=1)
        self.color_entry = tk.Entry(self)
        self.color_entry.grid(column=2, row=1)

        quantity_label = tk.Label(self, text="Enter the quantity")
        quantity_label.grid(column=0, row=2)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.grid(column=2, row=2)

        done_button = tk.Button(self, text="Finish the order",
                                command=self.get_chair_data)
        done_button.grid(column=1, row=4)


        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(column=1, row=5)

    def get_chair_data (self):
        global number

        size = self.size_entry.get()
        sheet.write(number, 1, "Chair")
        sheet.write(number, 2, size)

        color = self.color_entry.get()
        sheet.write(number, 3, color)

        quantity = int(self.quantity_entry.get())
        sheet.write(number, 4, quantity)

        number += 1

        workbook.save("May 2018 orders.xls")


class Table(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        size_label = tk.Label(self, text="Enter the size")
        size_label.grid(column=0, row=0)
        self.size_entry = tk.Entry(self)
        self.size_entry.grid(column=2, row=0)

        color_label = tk.Label(self, text="Enter the color")
        color_label.grid(column=0, row=1)
        self.color_entry = tk.Entry(self)
        self.color_entry.grid(column=2, row=1)

        quantity_label = tk.Label(self, text="Enter the quantity")
        quantity_label.grid(column=0, row=2)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.grid(column=2, row=2)

        done_button = tk.Button(self, text="Finish the order",
                                command=self.get_table_data)
        done_button.grid(column=1, row=4)

        button2 = tk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))

        button2.grid(column=1, row=5)


    def get_table_data(self):
        global number

        size = self.size_entry.get()
        sheet.write(number, 1, "Table")
        sheet.write(number, 2, size)

        color = self.color_entry.get()
        sheet.write(number, 3, color)

        quantity = int(self.quantity_entry.get())
        sheet.write(number, 4, quantity)

        number += 1

        workbook.save("May 2018 orders.xls")


app = App()
app.geometry("500x500")
app.mainloop()
