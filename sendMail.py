import smtplib
import sys
import getpass 
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text, passw, files=None):

    smtp = smtplib.SMTP("smtp.gmail.com: 587")
    smtp.starttls()
    smtp.login(send_from, passw)


    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = COMMASPACE.join(send_to)
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))

        part["Content-Disposition"] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    print("Succesfully Sent Mail!!")


def main():

    #"merinfrancis97@gmail.com","jobymathew.mec@gmail.com","riatreesa@gmail.com",
    bodystr = "This is a system generated mail!"
    attchment = ["protest.png", "embedlog.logAES"]
    to = sys.argv[1]

    inpto = open(sys.argv[1],"r")
    to = inpto.read()

    inp = open(sys.argv[2],"r")
    subjj = inp.read()

    to = to.split(" ")
    myAcc = "madpeach97@gmail.com"
    passwrd = "password"
    send_mail(myAcc, to, subjj, bodystr, passwrd, attchment)


if __name__ == "__main__":
    main()
