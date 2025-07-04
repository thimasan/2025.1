import socket, sys

msgs = ['ola', 'isso', 'eh', 'echo', 'client']

HOST = '10.25.1.189'
PORT = 12345

if len(sys.argv) == 2:
    HOST = sys.argv[1]
else:
    print (f'uso: sys.argv[0] servidor')
    print (f'     servidor default é {HOST}')
    print (f'continuando ...')

tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSock.connect((HOST, PORT))

nMsg = 0
while nMsg < 6:
    msg = msgs[nMsg%len(msgs)]
    tcpSock.send(msg.encode())
    reply = tcpSock.recv(1024)
    print (f'enviei {msg} -> recebi {reply.decode()}')
    nMsg += 1    
    
tcpSock.close()