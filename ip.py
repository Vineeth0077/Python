# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 00:45:48 2022

@author: chitr
"""

import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)

