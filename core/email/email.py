import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailBotSender():
    def __init__(self, from_email, password, to_email, subject, message, smtp):
        self.from_email = from_email
        self.password = password
        self.to_email = to_email
        self.subject = subject
        self.message = message
        self.smtp = smtp
        self.port = smtplib.SMTP_SSL_PORT

    def emailSender(self):
            try:
                debuglevel = 1

                smtp = smtplib.SMTP_SSL(self.smtp, self.port)
                smtp.set_debuglevel(debuglevel)
                smtp.login(self.from_email, self.password)

                msg = MIMEText(str(self.message), 'plain', 'utf-8')
                msg['Subject'] = Header(self.subject, 'utf-8')
                msg['From'] = self.from_email
                msg['To'] = self.to_email

                smtp.sendmail(msg['From'], msg['To'], msg.as_string())
                smtp.quit()
            except(EOFError):
                if os.path.isdir('output') != 1:
                    os.makedirs('output')
                    with open(os.path.abspath('output/Error_accounts.txt'), 'w') as f:
                        errors = self.from_email + '//' + self.to_email + '\n'
                        f.write(errors)

                else:
                    with open(os.path.abspath('output/Error_accounts.txt'), 'a') as f:
                        errors = self.from_email+ '//' + self.to_email + '\n'
                        f.write(errors)
