import requests, argparse
import argparse
import sys
from colorama import *

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url", required=True)
parser.add_argument("-p", "--payloads", help="payloads list", required=True)

def fuzz(url, payloads):
    for payloads in open (payloads, "r").readlines():
        new_url = url.replace('{fuzz}', payloads)
        request = requests.get(new_url)
        if request.elapsed.total_seconds > 7:
            print(Style.BRIGHT + Fore.RED + "Timedout detected with", new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + "Not Working On This Payload!", payloads)

def verif(url):
    url_test = url.replace("{fuzz}", "")
    req = requests.get(url_test)
    if req.elapsed.total_seconds > 6:
        sys.exit(Style.BRIGHT + Fore.RED + "Error! Please Try It Again!")
        
    else:
        fuzz(argparse.url, argparse.payloads)
    
if not '{fuzz}' in argparse.url:
    sys.exit(Style.BRIGHT + Fore.RED + "Missing {fuzz} parameter!")
    
else:
    verif(argparse.url)