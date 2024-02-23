import threading
import time

class MyThread(threading.Thread):
    # Costruttore:
    # Il parametro mi indica semplicemente l'ID numerico del thread
    def __init__(self, progID):
        # Eseguo il costruttore della classe base
        super(MyThread, self).__init__()
        
        # Attributi della classe
        self.__progID = progID
         
        # Per gestire la sospensione e la ripresa del thread
        self.__monitor = threading.Condition()
        # La richiesta di sospensione non è immediata...
        self.__toPause = False
        
    # Metodo per la richiesta di sospensione del thread
    def ThPause(self):
        self.__toPause = True
        # Voglio che questo metodo sia bloccante finchè il thread
        # non risulta effettivamente SOSPESO!
        with self.__monitor:
            pass
        
        # Istruzioni equivalenti
        # self.__monitor.acquire()
        # self.__monitor.release()
    
    # Metodo per la richiesta di ripresa del thread
    def ThResume(self):
        with self.__monitor:
            print(f"{self.__progID}: thread RIPRESO")
            self.__toPause = False
            # Invio la notifica di ripresa al thread
            self.__monitor.notify()
    
    def run(self):
        with self.__monitor:
            # ciclo infinito per non far terminare il thread
            while True:
                # controllo se mi è stato chiesto di sospendermi
                if self.__toPause:
                    print(f"{self.__progID}: thread SOSPESO")
                    # Sospensione effettiva del thread
                    self.__monitor.wait()
                
                print(f"{self.__progID}: thread in esecuzione...")
                time.sleep(0.1)