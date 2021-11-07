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
# birthday_file  # Debugging

# Get today's date:
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
# print(year, month, day)  # Debugging

# Look for a birthdate equal to today's date:
same_month = birthday_file[birthday_file["month"] == month]
birthday = same_month[same_month["day"] == day]
receiver_email = birthday.email.values[0]

# access a random letter template and add the person's name:
number = random.randint(1, 3)
complete_letter = ""
with open(f"./letter_templates/letter_{number}.txt") as letter:
    raw_letter = letter.readlines()
    for line in raw_letter:
        if "[NAME]" in line:
            modified_line = line.replace("[NAME]", birthday.name.values[0])
            complete_letter += modified_line
        else:
            complete_letter += line

# Send the e-mail:
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=receiver_email,
        msg=f"Subject:Happy Birthday!!!\n\n{complete_letter}"
    )
