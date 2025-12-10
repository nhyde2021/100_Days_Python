import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "neil.hyde17@gmail.com"
MY_PASSWORD = "hikvkduiocixfwxl"

def choose_letter():
    random_num = random.randint(1,3)
    letter = f"letter_templates/letter_{random_num}.txt"
    return letter

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
today = (dt.datetime.now().month, dt.datetime.now().day)


if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter_selection = choose_letter()
    with open(letter_selection) as file:
        file_data = file.read()
        file_data = file_data.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{file_data}"
        )