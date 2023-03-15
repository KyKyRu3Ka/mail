import os


def email_start(threads):
    for _ in range(threads):
        email_attack()


def email_attack():
    emails = []
    for_emails = []

    with open(os.path.abspath('input/for_email_accounts.txt'), 'r') as file:
        for line in file:
            for_emails.append(line.replace('\n', ''))

    with open(os.path.abspath('input/email_accounts.txt'), 'r') as file:
        for line in file:
            emails.append(line.replace('\n', ''))

    for em, to_email in zip(emails, for_emails):
        if em.find('@yahoo.com') != -1:
            smtp_ = 'smtp.mail.yahoo.com'
        elif em.find('@mail.ru') != -1:
            smtp_ = 'smtp.mail.ru'
        elif em.find('@bk.ru') != -1:
            smtp_ = 'smtp.mail.ru'
        else:
            smtp_ = 'smtp.rembler.ru'

        line = em.split(':')
        from_email = line[0]
        from_pas = line[1]

        try:
            from smtplib import SMTP_SSL, SMTP_SSL_PORT
            from email.mime.text import MIMEText
            from email.header import Header

            debuglevel = 0

            smtp = SMTP_SSL(smtp_, port=SMTP_SSL_PORT)
            smtp.set_debuglevel(debuglevel)
            smtp.login(from_email, from_pas)

            msg = MIMEText('Текс', 'plain', 'utf-8')
            msg['Subject'] = Header('Заголовок', 'utf-8')
            msg['From'] = from_email
            msg['To'] = to_email

            smtp.sendmail(msg['From'], msg['To'], msg.as_string())
            smtp.quit()
        except:
            if os.path.isdir('output') != 1:
                os.makedirs('output')
                with open(os.path.abspath('output/Error_accounts.txt'), 'w') as f:
                    errors = from_email + '//' + to_email + '\n'
                    f.write(errors)

            else:
                with open(os.path.abspath('output/Error_accounts.txt'), 'a') as f:
                    errors = from_email + '//' + to_email + '\n'
                    f.write(errors)