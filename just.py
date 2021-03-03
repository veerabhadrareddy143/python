import smtplib
sender_mail="madithativeerabhadrareddy@gmail.com"
receiver_mail="madithatireddysekharreddy@gmail.com"
message="hi this is veera bhadra"
try:
    smtpObj=smtplib.SMTP("localhost")
    smtpObj.sendmail(sender_mail,receiver_mail,message)
    print("mail was sent")
exceptException:
    print('error')
