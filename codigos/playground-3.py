#Teste Condicionais IF/ELSE
saldoAtualCliente = 15
saldoProximoCliente = 10

if saldoAtualCliente < saldoProximoCliente :
    print("saldo do cliente atual e menor que o saldo do proximo cliente")

    fechamentoCaixa = saldoAtualCliente + saldoProximoCliente
    print(f"Vendas do dia: {fechamentoCaixa}")
else :
    print("saldo do cliente atual e maior que o saldo do proximo cliente")
    
    fechamentoCaixa = saldoAtualCliente + saldoProximoCliente - 8
    print(f"Venda do dia - 8 reais de gastos: {fechamentoCaixa}")