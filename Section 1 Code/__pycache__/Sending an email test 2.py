import smtplib
# import linfo

server = smtplib.SMTP("smtp.gmail.com", 587)

server.ehlo()

server.starttls()

server.login(linfo.email, linfo.password)

message =  "hi there just testing to see if this works"

subject = "Test1"

fmessage = "Subject: {}\n\n{}".format(subject, message)


server.sendmail("guille8454@gmail.com", "guille8454@gmail.com", fmessage)

server.quit()




