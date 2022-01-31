import aiohttp
import asyncio
from aiohttp_socks import ProxyConnector
import requests

unchecked_proxy = []
valid_proxy = []

def fetch():
    url = 'proxy list url'
    resp = requests.get(url)
    for line in resp.text.splitlines():
            unchecked_proxy.append(line)
    return unchecked_proxy

async def get(i):
    try:
        timeout = aiohttp.ClientTimeout(total=5)
        connector = ProxyConnector.from_url(f'socks5://{i}')
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            async with session.get('https://checkip.amazonaws.com/', ssl=False) as response:
                if response.status == 200:
                    valid_proxy.append(i)
    except:
        pass


unchecked = fetch()
loop = asyncio.get_event_loop()
coroutines = [get(_) for _ in unchecked]
result = loop.run_until_complete(asyncio.gather(*coroutines))
print(valid_proxy)
