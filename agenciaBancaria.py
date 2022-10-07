from conta import Conta



class AgenciaBancaria:
    def __init__(self, codigo):
        self.__codigo=codigo
        self.__contas =[]
        
    def addContas(self, contaObj):
        self.__contas.append(contaObj)
        
    def getConta(self,numero):
        for conta in self.__contas:
            if conta.getNumero()==numero:
                return conta
        return None
    
    def listaContas(self):
        strContas =""
        for conta in self.__contas:
            strContas+= conta.getTitular()+" saldo R$ "+str(conta.getSaldo())+"\n"#\n pula a linha 
        return strContas
            
    