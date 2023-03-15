from core.email.email import *

threads = 1
target = 'leksikov678@yahoo.com'
message = 'Good Day!'
subj = 'Alert'
if __name__ == "__main__":
    email_start(threads, target, message, subj)
