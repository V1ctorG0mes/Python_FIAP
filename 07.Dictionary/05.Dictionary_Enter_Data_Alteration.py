#criando um dicionario vazio
dicionario = {}

#incluindo dados no dicionario
dicionario["André David"] = "Professor"

#alterando dados no dicionário
dicionario["André David"] = "Coordenador"


#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))