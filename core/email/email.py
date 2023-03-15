import os


def email_start(threads, email, mes, subj):
    for _ in range(threads):
        email_attack(email, mes, subj)


def email_attack(email, mes, subj):
    emails = []

    with open(os.path.abspath('input/email_accounts.txt'), 'r') as file:
        for line in file:
            emails.append(line.replace('\n', ''))
    for em in emails:
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
            import datetime

            debuglevel = 0

            smtp = SMTP_SSL(smtp_, port=SMTP_SSL_PORT)
            smtp.set_debuglevel(debuglevel)
            smtp.login(from_email, from_pas)

            from_addr = from_email
            to_addr = "leksikov678@gmail.co"

            subj = "Дароу!"
            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

            message_text = "Дароу\nЭто сообщение отправлено через бота!\n\nПока!\n"

            msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"\
            % (from_addr, to_addr, subj, date, message_text)

            smtp.sendmail(from_addr, to_addr, msg)
            smtp.quit()
        except:
            if os.path.isdir('output') != 1:
                os.makedirs('output')
                with open(os.path.abspath('output/Error_accounts.txt'), 'w') as f:
                    errors = from_email + '//' + to_addr + '\n'
                    f.write(errors)
            else:
                with open(os.path.abspath('output/Error_accounts.txt'), 'a') as f:
                    errors = from_email + '//' + to_addr + '\n'
                    f.write(errors)