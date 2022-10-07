from typing import Container


class Conta:
    def __init__(self,numero,titular):
        self.__numero=numero
        self.__titular=titular
        self.__saldo=0
        
        
    def getNumero(self):
        return self.__numero
    
    def getTitular(self):
        return self.__titular
    
    def getSaldo(self):
        return self.__saldo
    
    def depositar(self,valor):
        if valor >0:
            self.__saldo += valor
        else:
            print("insira um valor positivo")
        
    def sacar (self,valorsaque):
        if self.__saldo >= valorsaque:
            self.__saldo -= valorsaque
        else:
            print("saldo insuficiente")
    
        