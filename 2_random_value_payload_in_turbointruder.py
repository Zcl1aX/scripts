import random
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           engine=Engine.BURP # Use Burp's network stack, including upstream proxies etc
                           )

    for i in range(3, 8):
        engine.queue(target.req, randstr(i), learn=1)

    for a in range(1, 1000):
        f = open('/usr/share/dict/name', 'r')
        l = [line.strip() for line in f]
        name=random.choice(l)

        fph = open('/usr/share/dict/phone', 'r')
        l2 = [line2.strip() for line2 in fph]
        phone=random.choice(l2)


        engine.queue(target.req, [name.rstrip(), phone.rstrip()])

def handleResponse(req, interesting):
    if interesting:
        table.add(req)
        callbacks.addToSiteMap(req.getBurpRequest())
        # You can also trigger scans, report issues, send to spider, etc:
        # https://portswigger.net/burp/extender/api/burp/IBurpExtenderCallbacks.html
