import csv
import datetime
import os
import smtplib
from email.message import EmailMessage

def get_today_entry(quotes_file='stoic_quotes_output.csv'):
    try:
        today = datetime.datetime.now()
        day = today.day
        suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        today_str = today.strftime(f"%B {day}{suffix}")

        with open(quotes_file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='|')
            for row in reader:
                if row[0] == today_str:
                    return format_entry(row)

        return f"{today_str}\n\n\nNo stoic entry found for today."

    except Exception:
        return (
            "Today\n\n\n"
            "BRIGHT SIDE\n\n\n"
            "\u201cAlways Look on the Bright Side of Life.” —ERIC IDLE\n\n\n"
            "Sometimes life throws errors instead of wisdom. Today is one of those days."
        )

def format_entry(entry_row):
    date, title, quote, comment = entry_row
    formatted = f"{date}\n\n\n{title}\n\n\n{quote}\n\n\n{comment}"
    return formatted.replace("   ", "\n\n")

class DailyQuoteEmail:

    def __init__(self):
        self.quote_of_the_day = get_today_entry()

        self.recipients_list = [os.environ['EMAIL']]  # send to yourself

        self.sender_credentials = {
            'email': os.environ['EMAIL'],
            'password': os.environ['EMAIL_PASSWORD']
        }

    def send_email(self):
        msg = EmailMessage()
        msg['Subject'] = f"Daily Stoic Quote - {datetime.date.today().strftime('%d %b %Y')}"
        msg['From'] = self.sender_credentials['email']
        msg['To'] = ', '.join(self.recipients_list)
        msg.set_content(self.quote_of_the_day)

        with smtplib.SMTP('mail.gmx.com', 587) as server:
            server.starttls()
            server.login(self.sender_credentials['email'], self.sender_credentials['password'])
            server.send_message(msg)

if __name__ == '__main__':
    emailer = DailyQuoteEmail()
    emailer.send_email()
