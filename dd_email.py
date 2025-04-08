import datetime
import smtplib
from email.message import EmailMessage
from dd_content_full import get_today_entry  # Your daily quote function

class DailyDigestEmail:

    def __init__(self):
        self.daily_quote = get_today_entry('stoic_quotes_output.csv')

        self.recipients_list = [
            'roman.popoff@yahoo.com.au',
            
        ]

        self.sender_credentials = {
            'email': 'YOUR SENDER EMAIL ADDRESS GOES HERE',
            'password': 'YOUR SENDER EMAIL PASSWORD GOES HERE'
        }

    def send_email(self):
        msg = EmailMessage()
        msg['Subject'] = f'Stoic Quote of the Day - {datetime.date.today().strftime("%d %b %Y")}'
        msg['From'] = self.sender_credentials['email']
        msg['To'] = ', '.join(self.recipients_list)

        msg.set_content(self.daily_quote)

        with smtplib.SMTP('mail.gmx.com', 587) as server:
            server.starttls()
            server.login(self.sender_credentials['email'], self.sender_credentials['password'])
            server.send_message(msg)

if __name__ == '__main__':
    email = DailyDigestEmail()

    # Preview quote
    print('\nToday\'s Stoic Quote Email Content:\n')
    print(email.daily_quote)

    # Send email
    print('\nSending email...')
    email.send_email()
