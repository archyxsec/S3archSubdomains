#!/usr/bin/python3
# Copyrigth by BerL1n
# A simply subdomains list implements by BerL1n using crt.sh

"Usage {0} <host>"

import requests
import sys
import re

# Colors for print format
from termcolor import colored

print(colored('Subdomains scan by Berl1n..', 'blue', attrs=['bold']))

# PRINCIPAL REQUEST
URL = "https://crt.sh/?CN=%25." + sys.argv[1]
r = requests.get(url=URL)
data = r.text
dat = data.splitlines()
s = "." + sys.argv[1]

# Main function


def urlUtil():
    print(colored("\nValid subdomains...", "blue", attrs=['bold']))
    coun = 0
    for line in dat:
        if re.search(s, line):
            d = line.split(">")[1]
            coun += 1
            if coun > 9:
               url = d.split("</")[0]
               req = "http://www." + url
               try:
                  urlrequest = requests.get(url=req)
                  if urlrequest.status_code == 200:
                     print(colored(url, 'red', attrs=['bold']))
               except requests.exceptions.ConnectionError:
                  pass


def AllUrl():
    print(colored("\nAll subdomains...", "blue", attrs=['bold']))
    counter = 0
    for line in dat:
        if re.search(s, line):
            final = line.split(">")
            counter += 1
            if counter > 9:
                print(colored(final[1].split("</")[0], 'red', attrs=['bold']))


def main():
    print(colored("\nWhich option do you want to select:",
                  "green", attrs=['bold']))
    print(colored("[1]", "green", attrs=['bold']) +
          colored(" All domains", "magenta", attrs=['bold']))
    print(colored("[2]", "green", attrs=['bold']) +
          colored(" Util domains(200 response code)", "magenta", attrs=['bold']))
    opcion = input(colored("Select an option: ", "green", attrs=['bold']))
    if opcion == '1':
        AllUrl()
    elif opcion == '2':
        urlUtil()
    else:
        print(colored("N0t a VAlid 0ption", "red", attrs=['bold']))


# ARGUMENT CHECK
if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

try:
    main()
except KeyboardInterrupt:
    pass
