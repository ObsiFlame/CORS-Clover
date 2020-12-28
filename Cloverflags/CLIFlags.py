#!/bin/python3 

import argparse
import sys
import time

USER_URL = None
USER_FILENAME = None

def cliflags():

    parser = argparse.ArgumentParser(description="CORS Clover a Cross-Origin Misconfiguration enumeration tool")
    parser.add_argument("--url", help='Provide the URL endpoint you want to test (-u https://<target.com>)', type=str, default='http://example.com')
    parser.add_argument('--output', help='Dumps the output if you want provide Y/N', type=str, default='Y')

    args = parser.parse_args()

    global USER_URL
    global USER_FILENAME

    USER_URL = args.url

    if args.output == 'Y':
        USER_FILENAME = 'output.json'
        time.sleep(1)

    elif args.output == 'N' or args.output != 'Y':
        USER_FILENAME = None
    
    else:
        raise TypeError("You haven't specified the right flag Y/N \n")
        sys.exit()

# Get the data from args 

def get_URL():
    return USER_URL
    
def get_FILENAME():
    return USER_FILENAME
