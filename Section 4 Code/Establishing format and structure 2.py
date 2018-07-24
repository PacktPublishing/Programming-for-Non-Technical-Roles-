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


c = canvas.Canvas(pdf_file_name, pagesize="letter")

c.setFont("Helvetica-Bold", 30, leading=True)


c.drawCentredString(325, 600, "May 2018 Report")

c.setFont("Helvetica-Bold", 25, leading=True)
c.drawCentredString(325, 560, "XYZ Company")

c.setFillColor(colors.deepskyblue)
c.rect(0,0, width=45, height=800, fill=True, stroke=True)

logo = "logo-1933884.png"

c.drawImage(logo, 230, 350, width=180, height=180)

c.showPage()

# page 2

# goals

c.setFont("Helvetica-Bold", 30, leading=True)

c.drawCentredString(100, 720, "Goals")

goals = [
    "Increase net operating income by 1.5%",
    "Renew the 10 year lease with Valmart",
    "Hire a certified information tecnology specialist",
    "Complete the construction of the 3 apartments at Sunny Drive",
    "Start renovation for Finch complex",
    "Finish the negotiation with Walter's",
    "Begining the due diligence of the 67,000 sqf at Hammers Road"
    ]

# results
c.setFont("Helvetica-Bold", 30, leading=True)
c.drawCentredString(100, 370, "Results")

results = [
    "1% Increase of net operating income",
    "Valmart 10 year lease renewed",
    "Two candidates are left to chose for the IT position",
    "Half of an apartment is left at Sunny Drive",
    "The renovation was approved and the construction started",
    "Walter's negotiation needs the agreement of clause T5",
    "Due diligence of Hammers Road completed"
]

c.showPage()

c.drawString(20,20, "its working")




c.save()