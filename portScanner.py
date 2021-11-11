#!/usr/bin/python3
import sys
import _thread
import time
from socket import *

def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((targetIP, port))
    if result == 0:
        lock.acquire()
        print(str(port) + ' ', end = '')
        lock.release()
        _thread.exit()

if __name__=='__main__':
    host = sys.argv[1]
    portRange = sys.argv[2].split('-')

    startPort = int(portRange[0])
    endPort = int(portRange[1])

    targetIP = gethostbyname(host)

    lock = _thread.allocate_lock()
    print('IP: %s'%(targetIP))
    print("Opened ports: ", end = '')
    for port in range(startPort, endPort):
        _thread.start_new_thread(tcp_test, (port,))
        time.sleep(1)