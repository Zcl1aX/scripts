import requests
from ipaddress import ip_network
from multiprocessing import Pool

search_mask = '0.0.0.0/24' 

def revip(ip):
    try:
        req = requests.get('https://'+ip, timeout=(5, 10))

    except requests.exceptions.SSLError as errc:
        errc = str(errc)
        errc = errc.replace(',','').replace("'","").split(' ')
        print("IP:",ip,"domein:", errc[6:])
   
    except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout) as errc:        
        print("IP:",ip,"domein: ConnError")

ips = ip_network(search_mask).hosts()

List_IP = []
for a in ips:
    List_IP.append(str(a))


pool = Pool(processes=30)
results = pool.map(revip, List_IP)

pool.close()
pool.join()
