import socket
import sys

def C(x):
    x = float(x)
    return str(x+20)


def run_server(host="localhost", port=8883):
    
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (host, port)
    
    print >> sys.stderr, 'starting up server C on %s port %s' % server_address
    
    sock.bind(server_address)
    sock.listen(1)
    
    while True:
        print >> sys.stderr, 'server C: waiting for a connection'
        
        connection, client_address = sock.accept()
        try:
            print >> sys.stderr, 'client connected:', client_address
            while True:
                x = connection.recv(16)
                print >> sys.stderr, 'received "%s"' % x
                if x:
                    result = C(x)
                    connection.sendall(result)
                else:
                    break
        finally:
            connection.close()
            

if __name__ == "__main__":
    run_server()