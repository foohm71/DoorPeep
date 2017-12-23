#!/usr/bin/env python

import os
from subprocess import check_output
import subprocess
import socket
import fcntl
import struct

homeDir = "/root/DoorPeep"
emailDir = "/root/DoorPeep/Email"
cameraDir = "/root/DoorPeep/Camera"

streamerProcName = "mjpg_streamer"
ntwkinterface = "apcli0"
port = "8080"

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def sendAlert(url):
   os.chdir(emailDir)
   os.system("./sendmail.py \"%s\"" % url)


def checkStreamer():
   try:
      # Everything is good ie. Streamer process running
      pid = check_output(["pidof", streamerProcName])
   except subprocess.CalledProcessError:
      # Streamer process has died
      os.chdir(cameraDir)
      os.system("./start.sh")
      url = "http://%s:%s" % (str(get_ip_address(ntwkinterface)), port)
      sendAlert(url)
      
if __name__ == '__main__':
   checkStreamer()
