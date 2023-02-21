from core.email.email import *

target = 'bro.maps@ya.ru'
threads = 1
message = 'Good Day!'
subj = 'Alert'
if __name__ == "__main__":
    email_start(threads, target, message, subj)
