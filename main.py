from core.email.email import *

target = 'leksikov678@gmail.com'
threads = 1
message = 'Good Day!'
subj = 'Alert'
if __name__ == "__main__":
    email_start(threads, target, message, subj)
