from conta import Conta
from agenciaBancaria import AgenciaBancaria



c1=Conta(1234,"Mateus Augusto")
c2=Conta(5678,"Patric")
agencia=AgenciaBancaria(998)
agencia.addContas(c1)
agencia.addContas(c2)
#c1.depositar(500)
agencia.getConta(1234).depositar(1000)
agencia.getConta(5678).depositar(200)
print(agencia.listaContas())


agencia.getConta(1234).sacar(80)
agencia.getConta(5678).sacar(50)

print(agencia.listaContas())



