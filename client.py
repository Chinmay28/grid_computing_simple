import socket
import sys
import re


def clientop(number, op):
    
    port = 8880 + op

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', port)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    
    try:
        # Send data
        message = str(number)
        print >> sys.stderr, 'sending "%s"' % message
        sock.sendall(message)
    
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data
    
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
        return float(data)
        

def A(num):
    return clientop(num, 1)   
   
def B(num):
    return clientop(num, 2)  

def C(num):
    return clientop(num, 3)  

def D(num):
    return clientop(num, 4)  

def E(num):
    return clientop(num, 5)  


     
'''main'''
string = raw_input().strip()
x = int(re.search(r'\d+', string).group())
for expr in sys.stdin.readlines():
    print expr
    if expr == "\n":
        continue
    expr = expr.replace('x', str(x))
    print expr
    print eval(expr)
    
