import smtplib as sl
import os, ssl


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
            smtp = 'smtp.mail.yahoo.com'
        elif em.find('@mail.ru') != -1:
            smtp = 'smtp.mail.ru'
        else:
            smtp = 'smtp.rembler.ru'

    line = em.split(':')
    from_email = line[0]
    from_pas = line[1]
    print(from_email)
    print(from_pas)

    try:
        charset = 'Content-Type: text/plain; charset=utf-8'
        mime = 'MIME-Version: 1.0'
        text = "Отправкой почты управляет Python!"
        body = "\r\n".join((f"From: {from_email}", f"To: {email}",
                            f"Subject: {subj}", mime, charset, "", text))

        context = ssl.create_default_context()
        server = sl.SMTP(smtp)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(from_email, from_pas, initial_response_ok=True)
        server.sendmail(from_email, email, body.encode('utf-8'))
        server.quit()
        print('Suc')
    except(EOFError):
        print('Err')
