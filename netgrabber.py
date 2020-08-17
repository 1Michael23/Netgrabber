#    _   _      _    ____           _     _               
#   | \ | | ___| |_ / ___|_ __ __ _| |__ | |__   ___ _ __
#   |  \| |/ _ \ __| |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
#   | |\  |  __/ |_| |_| | | | (_| | |_) | |_) |  __/ |
#   |_| \_|\___|\__|\____|_|  \__,_|_.__/|_.__/ \___|_|

#Grabs the mac and ip from all attached network cards

import socket
import fcntl
import psutil
import netifaces as ni
from getmac import get_mac_address as gma

#define data

hostname = socket.gethostname()

addrs = psutil.net_if_addrs()

rawnics = (ni.interfaces())

f = open(hostname, 'w+')

#write hostname

f.write("Hostname:" + hostname +'\n\n')

#grab ip and mac from all adapters

for i in rawnics:
    ni.ifaddresses(i)
    ip = ni.ifaddresses(i)[ni.AF_INET][0]['addr']
    f.write(i+': Ip: '+ip+'\n')
    mac_address = gma(interface=i)
    f.write(i + ": Mac address: " + mac_address + '\n\n')

#write data

f.close()
