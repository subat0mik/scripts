#!/usr/bin/env python3

# Black Hat Python 2E
# TCP Server

import socket
import threading
IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))                                                                         # Specify IP and port to listen on
    server.listen(5)                                                                                # Start listening
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()                                                           # When a client connects...
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()                                                                      # Start thread to handle client connection

def handle_client(client_socket):                                                                   # Performs recv() then sends a simple message back to client
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()
