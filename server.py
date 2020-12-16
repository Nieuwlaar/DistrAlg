import msvcrt
import socket

from pip._vendor.distlib.compat import raw_input

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)

s2 = socket.socket()
port2 = 12346
s2.bind(('', port2))
s2.listen(5)

c, addr = s.accept()
c2, addr2 = s2.accept()
print ("Socket Up and running with a connection from",addr)

while True:
    rcvdData = c.recv(1024).decode()
    rcvdData2 = c2.recv(1024).decode()
    print("Message from C1:",rcvdData)
    print("Message from C2:", rcvdData2)
    sendData = raw_input("Send: ")
    c.send(sendData.encode())
    c2.send(sendData.encode())
    if (sendData == "Q"): # send Q to quit
        break

c.close()