import smtplib

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # This is what makes the mail secure (encrypted).
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="",
                        msg="Subject:Hello\n\nAnd this is the body of the email.")
    connection.close()
