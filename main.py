import re
from regex import *
import settings
import datetime


while 1:
    string = raw_input('> ')
    for regex, output in io:
        now = datetime.datetime.now()
        match = re.match(regex, string, re.I)
        if match:
            print(output.format(my_name=settings.CHATBOT,datetime=now,**match.groupdict()))
            break
