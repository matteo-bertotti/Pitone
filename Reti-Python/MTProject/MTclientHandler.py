import threading 

# Questo classe gestisce l connessione con un client estendendo la calsse THREAD e fa l'override del metodo RUN
class ClientHandler(threading.Thread):
    def __init__(self, clientSocket, clientAddress, clients):
        super(ClientHandler, self).__init__()
        self.__clientSocket = clientSocket
        self.__clientAddress = clientAddress
        self.__clients = clients
        # Per garantire l'accesso al socket in scrittura ad un singolo Thread, ho bisogno di un MUTEX
        self.__mutex = threading.Lock()

    # Metodo scrittura sul socket ad ACCESSO CONTROLLATO, solo un thread alla volta puo eseguire questo codice
    def write(self, message):
        # Accesso in mutaua esclusione 
        with self.__mutex:
            # Se sono all'interno di questo blocco ho l'accesso esclusivo al socket
            self.__clientSocket.send(message)
            
    # Override del metodo run        
    def run(self):
        # Se qualcosa va stroto, abbandono il client
        try:
            # Recupero IP e Porta del client e lo mostro sullo schermo
            (ipClient, PortClient) = self.__clientAddress
            print(f"WOW!! E' arrivato un nuovo amico! {ipClient}:{PortClient}")
            # Ciclo infinito diattesa messaggi da parte di un client 
            while True:
                # Leggo messsaggio inviato da client
                data = self.__clientSocket.recv(1024)
                if not data:
                    break
                # Dati in arrivo considerati come STRINGHE
                decodedData = data.decode("utf-8")
                # Preparo un messaggio da inviare a tutti i client
                answer = f"{ipClient}:{PortClient}-->{decodedData}"
                # Ciclo su tutti i clientHandler presenti nel dizionario -- SIMULO COMPORTAEMENTO BROADCAST
                for k, c in self.__clients.items():
                    # Qualunque errore dovesse succedere qua dentro, durante l'invio dei messaggi, questo clientHandler non deve subire alcuna anomali. DEVE FREGARSENE
                    try:
                        # Uso metodo pubblic write di ogni clientHandler
                        c.Write(answer.encode("utf-8"))
                    except Exception:
                        pass    
            # Se sono qua sono uscito dal ciclo perche non sono arrivati dati
            self.__clientSocket.close()
        except Exception:
            pass
        finally:
            print(f"AHIA... Il client {self.__clientAddress} è morto")
            # Rimuovo il clientHandler dal dizionario
            # ATTENZIONE!! Questa istruzione è scritta con troppa LEGGEREZZA!!
            self.__clients.pop((ipClient, PortClient))
            