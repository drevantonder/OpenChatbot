import re
from regex import *
import datetime

CHATBOT = "Bob"

while 1:
    string = raw_input('> ')
    for regex, output in io:
        now = datetime.datetime.now()
        match = re.match(regex, string, re.I)
        if match:
            print(output.format(my_name=CHATBOT,datetime=now,**match.groupdict()))
            break
