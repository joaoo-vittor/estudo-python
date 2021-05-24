from aula13Contas.contaPoupanca import ContaPoupanca
from aula13Contas.cantaCorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)

cp.depositar(150)
cp.sacar(151)
cp.detalhes()
cp.sacar(150)

print('#'*20)

cc = ContaCorrente(agencia=2222, conta=3333, saldo=0)

cc.detalhes()
cc.depositar(200)
cc.sacar(250)
cc.sacar(50)
cc.sacar(0.01)
