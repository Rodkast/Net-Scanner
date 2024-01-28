#!/usr/bin/env python3
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    

    clients_list= []
    for element in answered_list:
        client_dict ={"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    
    print_result(clients_list)
    
    #return clients_list

def vendor(mac_original):
    mac_new = mac_original.replace(":", "").upper()
    with open ("vendor.txt") as f:
        for entry in f.readlines():
            prefix, vendor = entry.split("\t")[0], entry.split("\t")[1].strip()
            if mac_new.startswith(prefix):
                 return vendor  
            


def print_result(results_list):
    print("----------------------------------------------------------------------")
    print("IP\t\t\tMAC Address\t\t\tVENDOR\n----------------------------------------------------------------------")
    for client in results_list:
        vname = str(vendor(client['mac']))
        if vname == "None":
            vname = "Unknown"

        print(f"{client['ip']}\t\t{client['mac']}\t\t{vname}")

scan('192.168.1.1/24')  
