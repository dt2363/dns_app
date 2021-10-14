import json
import socket
import sys


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 53533))
    sock.listen(5)
    while True:
        clientConnected, clientAddress = sock.accept()
        print ('Got connection from', clientAddress)
        dataFromClient = clientConnected.recv(1024)
        print(dataFromClient.decode())
        break

# app.run(host='0.0.0.0',
#         port=53533,
#         debug=True)
