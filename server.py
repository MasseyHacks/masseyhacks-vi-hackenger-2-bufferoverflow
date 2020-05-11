import socket
import traceback
import multiprocessing


def comm(conn, addr):

    try:
        conn.sendall(b'Please send the 16-character password:')
        message = conn.recv(4096)
        #print(message)
        passwd = message.decode('utf8')
        #print(passwd)
        buffer = ['' for i in range(16)] + list("SE2m0yNX$83oHEvL")
        
        for i in range(len(passwd)):
            try:
                buffer[i] = passwd[i]
            except IndexError:
                buffer.append(passwd[i])
        

        if ''.join(buffer[:16]) == ''.join(buffer[16:32]):
            conn.sendall("AJD$!(#HD!B".encode('utf-8'))
        else:
            conn.sendall("Incorrect!".encode('utf-8'))

    except:
        conn.sendall(b'Error. Please try again')
        traceback.print_exc()

    conn.close()

if __name__ == '__main__':
    # do stuff

    connections = {}

    HOST = '127.0.0.1'
    PORT = 1511

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(999999)

    print('Server running on [%s:%i]' % (HOST, PORT))

    while True:

        try:

            conn, addr = server.accept()

            print('Incoming connection from [%s]' % str(addr))

            connections[addr] = multiprocessing.Process(target=comm, args=(conn, addr)).run()

        except:
            pass
