import socket

PORT = 50000
MYADDR = ('', PORT)
allClients = []

sockServer = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
try: 
    sockServer.bind(MYADDR)
    while True:
        try:
            data, source = sockServer.recvfrom(512)
            print (f"Recebido de {source}: {data.decode()}")            
            if source not in allClients:
                allClients.append(source)                
            for client in allClients:
                if source != client:
                    sockServer.sendto(data, client)
        except:
            print (f"Erro. Processamento de mensagem.")            
    socket.close()
except:
    print (f"Erro. Verifique se a porta {PORT} não está em uso.")