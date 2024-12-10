import numpy as np
#general
import time, threading
#Temporizador
def temporizador(tiempo, callback):
    def cuenta_regresiva():
        inicio = time.time()
        while time.time() - inicio < tiempo:
            print(time.time() - inicio)
            time.sleep(0.4998)
        callback()

    hilo = threading.Thread(target=cuenta_regresiva)
    hilo.start()
#Elixir
class  elixir():
    def __innit__(self,total):
        self.total = total
        self.usado = 0
        self.maximo = 10
        self.regeneracion = 0
    
    def consumir(self,cantidad):
        if self.total - self.usado > cantidad:
            self.usado += cantidad
            self.total -= cantidad
            return True
        return False
        
    def recuperar(self,cantidad):
        self.usado = max(0,self.usado-cantidad)

    def transferir(self,otro,cantidad):
        if self.total - self.usado < cantidad:
            self.usado += cantidad

#Resultados
def resultados():
    print(" - - Resultados - - ")

def match():
    temporizador(500,resultados)

#programa
if __name__ == '__main__':
    match()