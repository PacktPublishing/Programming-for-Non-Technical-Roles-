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

image = "frame-3302911_1280.jpg"

c = canvas.Canvas(pdf_file_name, pagesize="letter")

# c.drawImage(image, 0, 0, width=620, height=800)

c.setFont("Helvetica-Bold", 30, leading=True)


c.drawCentredString(325, 600, "May 2018 Report")

c.setFont("Helvetica-Bold", 25, leading=True)
c.drawCentredString(325, 560, "XYZ Company")

c.setFillColor(colors.deepskyblue)
c.rect(0,0, width=45, height=800, fill=True, stroke=True)

logo = "logo-1933884.png"

c.drawImage(logo, 230, 350, width=180, height=180)

c.showPage()

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


# page 3

# percentage revenue graph

workbook = xl.open_workbook("tenant_revenue_percentage.xlsx")

sheet = workbook.sheet_by_name("Sheet1")

tenants = sheet.col_values(0, 1, sheet.nrows)

percentage_revenue = sheet.col_values(1, 1, sheet.nrows)



plt.pie(percentage_revenue, labels=tenants, colors=[
    "red", "blue", "yellow", "purple", "green", "gray", "brown", "orange"], autopct = "%1.1f%%",shadow=True)

plt.title("Percentage of Revenue by Tenant")
plt.show()
plt.savefig("tenant_revenue.png")
plt.close()

import matplotlib.ticker as tkr

# monthly revenue graph

revworkbook = xl.open_workbook("monthly_revenue.xlsx")

revsheet = revworkbook.sheet_by_name("Sheet1")

months = revsheet.col_values(0, 1, revsheet.nrows)

revenues = revsheet.col_values(1,1,revsheet.nrows)


def xfunc(x, pos):
    s = "{:0,d}".format(int(x))
    return s

formatter = tkr.FuncFormatter(xfunc)

fig, ax = plt.subplots()

ax.yaxis.set_major_formatter(formatter)

plt.bar(months, revenues)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Revenue per Month")
# plt.show()
plt.savefig("monthly_revenue.png")
plt.close()


# noi graph


rev_iworkbook = xl.open_workbook("revenue_income.xlsx")

rev_isheet = rev_iworkbook.sheet_by_name("Sheet1")

months2 = rev_isheet.col_values(0, 1, rev_isheet.nrows)

rev = rev_isheet.col_values(1,1,rev_isheet.nrows)

noi = rev_isheet.col_values(2,1,rev_isheet.nrows)

formatter2 = tkr.FuncFormatter(xfunc)

fig, ax = plt.subplots()

ax.yaxis.set_major_formatter(formatter2)


plt.plot(months, rev)
plt.plot(months, noi)
plt.xlabel("Month")
plt.ylabel("Amount")
plt.title("Revenue/Net Operating Income")

plt.legend(["Revenue", "NET Operating Income"])

plt.show()
# plt.savefig("revenue_noi.png")
plt.close()

# graphs

noi_rev = "revenue_noi.png"

month_rev = "monthly_revenue.png"

tenant_rev = "tenant_revenue.png"


c.save()