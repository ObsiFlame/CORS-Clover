![CORS Clover](Assets/CORS-Clover.png)

## Description 
CORS-Clover uses python request for sending request to the website (endpoint), after the requests response is recieved by the script it parses the HTTP headers and shows you the important headers like
Allow-Control-Allow-Origin, Allow-Control-Allow-Methods, Access-Control-Allow-Credentials. Which are required as necessary to understand the CORS vulnerabilty and further you can do your testing with the end point. Well CORS-Clover dumps the results in output.json  

## Features
 
- Provide endpoints and automate the endpoint scan for CORS(Security Misconfiguration)
- Dumping the headers into a JSON file 
- Add multiple endpoint enumeration 

## Requirements
- Python 3.8.6  
- requests 
- [JQ json processor](https://stedolan.github.io/jq/)

## Running CORS Clover on Mac or Linux

``` git clone https://github.com/DexterLex98/CORS-Clover.git
    cd CORS-Clover
    pip3 install -r requirements.txt
    python3 clover.py -h 
    python3 clover.py --url <target_host_endpoint> --output <Y/N>
```
