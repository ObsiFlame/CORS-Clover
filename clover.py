#!/bin/python3

import requests as req
import sys
import os
import json
from Banner.info import banner
from Cloverflags.CLIFlags import cliflags
from Cloverflags.CLIFlags import get_URL, get_FILENAME

# Banner of the Project 
banner()

# CLI flags 
cliflags()

# Fetching user data from args

file_name = get_FILENAME()
url = get_URL()


# make add the sites to the list

class Websites:
    
    def __init__(self, domain , headers, json_filename):
        self.domain = domain
        self.headers = headers
        self.json_filename = json_filename
    
    def DumpWebsites_json(self):
        with open("raw.json", 'w') as file:
            json.dump(dict(self.headers), file)
            file.close()

    def beautify_json(self):
        command = f"cat raw.json | jq | tee -a {self.json_filename}"
        os.system(command)
    
    def clean_up(self):
        os.remove('raw.json')
        SystemExit
           
#Custom Header with evil.com
cus_header = {'Origin':'https://evil.com'}


def send_request(url, U_headers):
    cur_url = url 
    get_request_data  = req.get(cur_url,headers = U_headers)
    return get_request_data

try:
    # Here we'll send the request with a custom header of CORS
    
    url_request_data = send_request(url,cus_header)
    url_headers = url_request_data.headers 
        
    # Enumeration main process is done here
    
    target_url = Websites(url, url_headers, file_name)
    target_url.DumpWebsites_json()
    target_url.beautify_json()
    target_url.clean_up()

except IndexError: 
   print(f"You have to provide the URL !")
   raise(SystemExit)

