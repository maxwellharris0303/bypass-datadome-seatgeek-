import requests

url = 'https://ip.smartproxy.com/json'
proxy = 'geo.iproyal.com:12321'
# proxy = 'gate.smartproxy.com:15555'
username = 'GKCyVlsgbSptcyhV'
password = 'visPrxyBbs61_country-tr'

proxies = {
    'http': f'http://{username}:{password}@{proxy}',
    'https': f'http://{username}:{password}@{proxy}'
}

response = requests.get(url, proxies=proxies)
print(response.json())