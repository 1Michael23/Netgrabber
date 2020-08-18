#    _   _      _    ____           _     _
#   | \ | | ___| |_ / ___|_ __ __ _| |__ | |__   ___ _ __
#   |  \| |/ _ \ __| |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
#   | |\  |  __/ |_| |_| | | | (_| | |_) | |_) |  __/ |
#   |_| \_|\___|\__|\____|_|  \__,_|_.__/|_.__/ \___|_|

#Grabs the mac from all attached network cards

import socket,psutil,os
import netifaces as ni
from getmac import get_mac_address as gma
#define data

hostname = socket.gethostname()

addrs = psutil.net_if_addrs()

rawnics = (ni.interfaces())

f = open(hostname, 'w+')

f.write("Hostname: " + str(hostname) + '\n\n')

#grab ip and mac from all adapters

for i in rawnics:
    try:
        ip = ni.ifaddresses(i)[2][0]['addr']

    except KeyError:
        ip = "Skipped (No IP Found)"
    if os.name == 'nt':
        mac_address = ni.ifaddresses(i)[-1000][0]['addr']
    elif os.name == 'posix':
        mac_address = gma(interface=i)
    #writes the hostname, ip(s) and mac address(s) to the text file
    f.write(i + ': Ip: '+str(ip)+'\n' + i + ": Mac address: " + str(mac_address) + '\n\n')

#saves data and releases text file

f.close()
