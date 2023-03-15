from core.email.email import MailBotSender
import os


def StartBotSender():

    smtps = ''
    from_emails = []
    to_emails = []
    messages = ''
    subject = ''

    with open(os.path.abspath('input/Text_email.txt'), 'r', encoding='utf-8') as file:
        subject = next(file).strip()
        for line in file:
            messages += line

    with open(os.path.abspath('input/for_email_accounts.txt'), 'r') as file:
        for line in file:
            to_emails.append(line.replace('\n', ''))

    with open(os.path.abspath('input/email_accounts.txt'), 'r') as file:
        for line in file:
            from_emails.append(line.replace('\n', ''))

    for em, to_email1 in zip(from_emails, to_emails):
        if em.find('@yahoo.com') != -1:
            smtps = 'smtp.mail.yahoo.com'
        elif em.find('@mail.ru') != -1 or em.find('@bk.ru') != -1:
            smtps = 'smtp.mail.ru'
        else:
            with open(os.path.abspath('output/Error_accounts.txt'), 'a', encoding='utf-8') as file:
                file.write(em + ' Нету SMPT\n')
                pass
        line = em.split(':')
        from_email = line[0]
        from_pas = line[1]
        to_email = to_email1
        bot = MailBotSender(from_email, from_pas, to_email, subject, messages, smtps)
        bot.emailSender()

StartBotSender()
