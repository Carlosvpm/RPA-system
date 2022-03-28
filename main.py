import time
from memory import get_memory
from sms import sms_sent


def main():
    get_memory()


while sms_sent == False:
    main()
    time.sleep(10)