#!/usr/bin/env python3
import socket
import json
import os 
#get ip_addr or some unique sign 
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
    
#use ip_addr or some unique sign to get its corresponding hosts
def get_inventory(ip_addr):
    # Define your dynamic inventory logic here
    file_path = f"./all_hosts/{ip_addr}.json"
    if(os.path.exists(file_path)):
        with open(file_path, "r") as json_file:
            hosts = json.load(json_file)
            print(json.dumps(hosts))
            
            
ip_address = get_ip_address()
# print(f"IP Address: {ip_address}")
get_inventory(ip_address)
    
