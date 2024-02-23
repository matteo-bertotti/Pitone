import socket
import threading

class TCPClient:
    # Costruttore
    def __init__(self, serverIPAddress, serverPort):
        self.__serverIPAddress = serverIPAddress
        self.__serverPort = serverPort
        self.__clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Trucco per far terminare tutti i thread del client
        self.__stopAllThreads = False

    # Avvio la connessione al server
    def start(self):
        # Cerco di connettermi con i parametri passati al costruttore
        connection = False
        try:
            self.__clientSocket.connect((self.__serverIPAddress, self.__serverPort))
        except Exception as e:
            print(f"Errore di connessione al server {(self.__serverIPAddress, self.__serverPort)}")
        else:
            print(f"Connessione a {(self.__serverIPAddress, self.__serverPort)} avvenuta con successo!")
            connection = True
        
        # Controllo se ho una connessione
        if connection:
            # Attivo 2 Thread di gestione
            receiverThread = threading.Thread(target=self.__Receiver, args=())
            receiverThread.start()
            senderThread = threading.Thread(target=self.__Sender, args=())
            senderThread.start()

    # Metodo privato avviato come thread per ricevere i messaggi dal server
    def __Receiver(self):
        try:
            while not self.__stopAllThreads:
                # Attendo un messaggio dal server
                receiverData = self.__clientSocket.recv(1024)

                if not receiverData:
                    self.__stopAllThreads = True
                    print("Ho perso la connessione con il server")

                # Mostra il messaggio a video
                decodedData = receiverData.decode("utf-8")
                print(f"{decodedData}")
        except Exception:
            pass
        finally:
            self.__stopAllThreads = True

    # Metodo privato avviato come thread per inviare i messaggi al server 
    def __Sender(self):
        try:
            while not self.__stopAllThreads:
                # Chiedo all'utente una stringa da inviare come messaggio
                data = str(input(""))
                # Invio il messaggio
                self.__clientSocket.send(data.encode("utf-8"))
            
            # Chiudo la connessione con il server
            self.__clientSocket.close()
        except Exception:
            pass
        finally:
            self.__stopAllThreads = True