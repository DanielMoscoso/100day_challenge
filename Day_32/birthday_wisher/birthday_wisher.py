# TODO: 1. Update the birthdays.csv
# TODO: 2. Check if today matches a birthday in the birthdays.csv
# TODO: 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# TODO: 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

birthday_file = pd.read_csv("./birthdays.csv")
birthday_file

# Send the e-mail:
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
