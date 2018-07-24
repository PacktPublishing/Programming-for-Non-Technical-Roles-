import xlrd as xl
import smtplib
import config

workbook = xl.open_workbook("outstanding_balances.xlsx")

sheet = workbook.sheet_by_name("Sheet1")

# need to slice the names so we only get the first name for the email
names = sheet.col_values(0, 1, sheet.nrows)
# print(names)

# list within a list
names2 = [x.split(" ")for x in names]
# print(names2)

names3 = [x[0]for x in names2]
# print(names3)


outstanding = sheet.col_values(2, 1, sheet.nrows)
# print(outstanding)

emails = sheet.col_values(1, 1, sheet.nrows)
# print(emails)

# create a dictionary with names and emails to use send the emails


dictionary = dict(zip(names3, emails))
print(dictionary)


# server = smtplib.SMTP("smtp.gmail.com", 587)
#
# server.ehlo()
#
# server.starttls()
#
# server.login(config.email, config.password)

# make the loop to send the emails

slice = 0
for name, email in dictionary.items():
    message = "Hi, %s.  \n\n\nOur records indicate that you owe us %s dollars" %(name, outstanding[slice])
    slice += 1
    subject = "Outstanding payment"
    message = 'Subject: {}\n\n{}'.format(subject, message)
    sendmailStatus = server.sendmail('guille8454@gmail.com', email, message)
#
#
# server.quit()