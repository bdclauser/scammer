import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# change url as needed
url = 'https://craigslist.pottsfarm.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

names = json.loads(open('package.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    # sends to server
    requests.post(url, allow_redirects=False, data={
        'auid2yjauysd2uasdasdasd': username,
        'kjauysd6sAJSDhyui2yasd': password
    })

    print('sending username %s and password %s' % (username, password))
