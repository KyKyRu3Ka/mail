import smtplib
import os, ssl
import yagmail


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
            port = 465
        elif em.find('@mail.ru') != -1:
            smtp = 'smtp.mail.ru'
            port = 587
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
        #server = smtplib.SMTP('localhost')
        #server.set_debuglevel(1)
        #server.sendmail(from_email, email, body.encode('utf-8'))
        #server.quit()
        mailsender = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        mailsender.debuglevel = 1
        mailsender.login(from_email, from_pas)
        mailsender.sendmail(from_email, email, f"""\
        Date:17/05/2017,2:18
        From: {from_email}
        To: {email}
        Subject: A test
        testing
        """)
        mailsender.quit()
        print('Suc')
    except(EOFError):
        print('Err')
