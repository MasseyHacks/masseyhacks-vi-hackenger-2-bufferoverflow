import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1511       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world')
    data = s.recv(1024)
    s.sendall(b'1111111111111111111111111111111111111111111111111111111')
    data = s.recv(1024)
    

print('Received', repr(data))
