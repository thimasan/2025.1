import socket, os

SERVIDOR = ""
PORTA    = 2121
PASTAARQ = "arquivos"

def escutaPorta():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVIDOR, PORTA))
    sock.listen(1)
    
def leComando():
    tamanhoComando = int.from_bytes(sockCon.recv(4), byteorder='big')
    comando = b''
    while tamanhoComando > 0:
        leitura = sockCon.recv(tamanhoComando)
        tamanhoComando -= len(leitura)
        comando += leitura
    return comando

def adicionaTamanho(dados):
    tamanho = len(dados)
    return tamanho.to_bytes(4, byteorder='big')+dados

def respondeComandoNulo():
    sockCon.send(adicionaTamanho(b''))

def respondeComandoDir():
    listaArquivos = os.listdir(PASTAARQ)
    listaArquivos = "\r\n".join(listaArquivos).encode()
    sockCon.send(adicionaTamanho(listaArquivos))
        
def processaComando(comando):
    if comando[:3] == b'DIR':
        respondeComandoDir()
    else:
        respondeComandoNulo()
    return
    
def main():
    global sockCon
    
    escutaPorta()    
    while True:
        sockCon, cliente = sock.accept()
        comando = leComando()
        processaComando(comando)
main()