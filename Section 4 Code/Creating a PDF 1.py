import xlrd as xl
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from reportlab.lib import colors


# page 1

pdf_file_name = "May 2018 Monthly Report.pdf"

# image = "frame-3302911_1280.jpg"

c = canvas.Canvas(pdf_file_name, pagesize="letter")

c.setFont("Helvetica-Bold", 30, leading=True)

# x, y
c.drawCentredString(325, 600, "May 2018 Report")

c.setFont("Helvetica-Bold", 25, leading=True)
c.drawCentredString(325, 560, "XYZ Company")


c.setFillColor(colors.deepskyblue)
c.rect(0,0, width=45, height=800, fill=True, stroke=True)

logo = "logo-1933884.png"

c.drawImage(logo, 230, 350, width=180, height=180)

c.showPage()


c.save()