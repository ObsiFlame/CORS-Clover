#!/bin/python3

import requests as req
import sys
import os
import json
from Banner.info import banner
# Banner of the Project 

banner()

# make add the sites to the list

class Websites:
    
    def __init__(self, domain , headers, json_filename):
        self.domain = domain
        self.headers = headers
        self.json_filename = json_filename
    
    def DumpWebsites_json(self):
       # print(f"{self.domain} -> domain \n\n ")
       # print(f"{self.headers} -> header \n\n ")
        with open(f"{self.json_filename}", 'w') as file:
            json.dump(dict(self.headers), file)
            file.close()

    def beautify_json(self):
        command = f"cat {self.json_filename} | jq | tee -a output.json"
        with open(f"{self.json_filename}", 'r') as file:
            file_data = file.read()
            file.close()
            os.system(command)
           
#Custom Header
cus_header = {'Origin':'https://evil.com'}


def send_request(url, U_headers):
    cur_url = url 
    get_request_data  = req.get(cur_url,headers = U_headers)
    return get_request_data

try:
    url = sys.argv[1]       # Domain Value
    # Here we'll send the request with a custom header of CORS
    url_request_data = send_request(url,cus_header)
    url_headers = url_request_data.headers 
    # print(url_headers.values)
    
    # Crafting the Websites 
    
    website1 = Websites(url, url_headers, "domain.json")
    website1.DumpWebsites_json()
    website1.beautify_json()

except IndexError: 
   print(f"You have to provide the URL !")
   raise(SystemExit)

