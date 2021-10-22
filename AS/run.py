import json
import socket
import sys


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 53533))
    while True:
        try:
            client_data, client_address = server_socket.recvfrom(1024)
            print ('Got connection from', client_address, client_data)
            client_data = client_data.decode()
            print("client_data: ", client_data, type(client_data))
        except socket.error as e:
            print(e)
            response = {
                "message": "Bad Request",
                "status_code": 400
            }
            return 400
        with open("dns.json", "w+") as dns_file:
            dns_file.write(client_data)
        server_socket.close()
        break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Shutting Down DNS Server')
        sys.exit(0)
