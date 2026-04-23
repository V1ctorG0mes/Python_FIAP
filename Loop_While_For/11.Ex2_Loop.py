num_transacoes = int(input("Quantas transações você fez hoje? "))
soma_transacoes = 0

for transacoes in range(1, num_transacoes + 1,1):
    val_transacoes = float(input("Digite o valor da {} transação: ".format(transacoes)))
    soma_transacoes = soma_transacoes + val_transacoes

med_transacoes = soma_transacoes / num_transacoes

print("Você fez {} transações que deram um total de R${:.2f}".format(num_transacoes, soma_transacoes))
print(f"A média dessas transações foram R${med_transacoes:.2f}")