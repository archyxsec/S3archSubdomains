#!/usr/bin/python3
#Copyrigth by BerL1n

#https://www.crt.sh/?CN=%25.twitter.com

"Usage {0} <host>"

import requests
import sys
import re

if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

URL = "https://crt.sh/?CN=%25." + sys.argv[1]

r = requests.get(url = URL)

data = r.text

for line in data:
    print(line)
    if re.search(sys.argv[1], line):
        print(line)
