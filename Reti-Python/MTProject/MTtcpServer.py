import socket

class TCPServer:
    # Costruttore: qui si defeiniscono anche gli attributi della classe
    def __init__(self, port):
        # Indirizzo di ascolto server
        self.__ipAddress = "0.0.0.0"
        # Porta di ascolto
        self.__port = int(port)
        # Definisco il socket TCP
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Dizionario di clients connessi 
        self.__clients = {}

    def getIpAddress(self):
        return self.__ipAddress
    
    def getPort(self):
        return self.__port
    
    # Avvio GRANDE PUFFO
    def start(self):
        connection = False

        try:
            self.__socket.bind((self.__ipAddress, self.__port))
            self.__socket.listen(10)
            connection = True
        except Exception as ex:
            print(f"Errore di avvio del server: {str(ex)}")

