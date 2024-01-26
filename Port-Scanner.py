#!/usr/bin/env python3
import socket
import threading
import time 
from queue import Queue

socket.setdefaulttimeout(0.55)
print_lock = threading.Lock()

Target = input("Enter the Target IP:")
print ('Scanning Host for Open Ports:')

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conx = s.connect((Target, port,))
        
        with print_lock:
            print(f'[+] Port {port} is open!')
        
        conx.close()
    except:
        pass
        
    
def threader():
    while True:
        worker = q.get()
        port_scan(worker)
        
        q.task_done()
q = Queue()

starttime = time.time()

for x in range (200):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
    
for worker in range (1, 65535):
    q.put(worker)
    
q.join()

runtime = float("%0.2f" % (time.time() - starttime))
print("Run Time: ", runtime, "seconds")


    
    
    
    
    
    
            