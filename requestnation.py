#!/bin/python3

import requests as req
import sys
import json 

print("Finding CORS Bugs \n\n")

# make add the sites to the list

class Websites:
    
    def __init__(self, domain , headers):
        self.domain = domain
        self.headers = headers
    
    def DumpWebsites_json(self):
       # print(f"{self.domain} -> domain \n\n ")
       # print(f"{self.headers} -> header \n\n ")
        with open("domain.json", 'w') as file:
            json.dump(dict(self.headers), file)

           
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
    
    website1 = Websites(url, url_headers)
    website1.DumpWebsites_json()

except IndexError: 
   print(f"You have to provide the URL !")
   raise(SystemExit)

