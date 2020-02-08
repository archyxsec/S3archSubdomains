#!/usr/bin/python3
#Copyrigth by BerL1n
#A simply subdomains list implements by BerL1n using crt.sh

"Usage {0} <host>"

import requests
import sys
import re

#Colors for print format
from termcolor import colored

print(colored('Subdomains scan by Berl1n..', 'blue'))

if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

URL = "https://crt.sh/?CN=%25." + sys.argv[1]

r = requests.get(url = URL)

data = r.text

dat = data.splitlines()

s = "." + sys.argv[1]

counter = 0

for line in dat:
    if re.search(s, line):
       final = line.split(">")
       counter += 1
       if counter > 9:
       	   print(colored(final[1].split("</")[0],'red'))
