#!/usr/bin/env python

from netmiko import ConnectHandler

R1_DR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.1',
    'username': 'cisco',
    'password': 'cisco',
}

R2_BDR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.2',
    'username': 'cisco',
    'password': 'cisco',
}

R3_DRO = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.3',
    'username': 'cisco',
    'password': 'cisco',
}

R4_DRO = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.4',
    'username': 'cisco',
    'password': 'cisco',
}

R5_DRO = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.5',
    'username': 'cisco',
    'password': 'cisco',
}


DR=["router ospf 1","network 1.0.0.0 0.255.255.255 area 0","network 192.168.122.1 0.255.255.255 area 0","router-id 1.1.1.10","exit","int f0/0","ip ospf authentication"
        ,"ip ospf auth message-digest","ip ospf message-digest-key 1 MD5 ccna"]

BDR=["router ospf 1","network 2.0.0.0 0.255.255.255 area 0","network 192.168.122.2 0.255.255.255 area 0","router-id 1.1.1.9","exit","int f0/0","ip ospf authentication"
        ,"ip ospf auth message-digest","ip ospf message-digest-key 1 MD5 ccna"]


net_connect = ConnectHandler(**R1_DR)
outputDR = net_connect.send_config_set(DR)
print outputDR

net_connect = ConnectHandler(**R2_BDR)
outputBDR = net_connect.send_config_set(BDR)
print outputBDR

all_devices = [R3_DRO, R4_DRO, R5_DRO]

for devices in all_devices:
    if devices == R3_DRO :
        file = 'R3_DRO.txt'
    elif devices == R4_DRO :
        file == 'R4_DRO.txt'
    else:
        file == 'R5_DRO.txt'

    with open(file) as f:
    lines = f.read().splitlines()
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output
