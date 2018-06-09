"""
Alarm clock displays date and time to the second. 
Allows user to set alarm in hh:mm. 
At user set time, beeps every second for one minute. 
"""
import datetime
import time
from time import strftime
import sys

def is_time_format(alarm):
    import re
    patterns = ["\\b[0-1][0-9]:[0-5][0-9]\\b", "\\b[2][0-3]:[0-5][0-9]\\b", "\\b[0-9]:[0-5][0-9]\\b"]
    for pattern in patterns:
        if re.search(pattern, alarm):
           return True

def set_alarm():
    while 1:
        alarm = input("What time would you like the alarm to beep? Enter hh:mm ")
        if not is_time_format(alarm):
            print("Enter time as hh:mm using integers, hours < 24, min < 60.")
            continue
        break
    h = int(alarm.split(':')[0])
    m = int(alarm.split(':')[1])
    print("Alarm will beep for one minute starting at ", alarm)
    while True:
        print (strftime("%m/%d/%Y %H:%M:%S"), end = '', flush = True)
        print("\r", end = '', flush = True)
        time.sleep(1)
        if time.localtime()[3:5] == (h, m):
            sys.stdout.write('\a')
            sys.stdout.flush()
            
set_alarm()