import msvcrt
import socket

from pip._vendor.distlib.compat import raw_input

s = socket.socket()
s.connect(('127.0.0.1',12345))

while True:
    str = raw_input("Send: ")
    s.send(str.encode());
    received_msg_server = s.recv(1024).decode()
    print("From server: ", received_msg_server)
    if (received_msg_server == "Q"):  # quit on Q from server
        break

s.close()