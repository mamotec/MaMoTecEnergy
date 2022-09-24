#!/bin/python

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

# Create an instance of ModbusServer
server = ModbusServer("127.0.0.1", no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    while True:
        DataBank.set_words(0, [int(uniform(0, 100))])
        DataBank.set_words(1, [int(uniform(0, 100))])
        DataBank.set_words(2, [int(uniform(0, 100))])
        DataBank.set_words(3, [int(uniform(0, 100))])
        DataBank.set_words(4, [int(uniform(0, 100))])
        DataBank.set_words(5, [int(uniform(0, 100))])
        DataBank.set_words(6, [int(uniform(0, 100))])
        DataBank.set_words(7, [int(uniform(0, 100))])
        
        sleep(1)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")