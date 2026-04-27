#criando um dicionario com dados
dicionario = {
    "Yoda":"Mestre Jedi", #Chave Yoda está relacionada ao Valor Mestre Jedi
    "Mace Windu": "Mestre Jedi", 
    "Anakin Skywalker":"Cavaleiro Jedi", 
    "R2-D2":"Dróide", 
    "Dex":"Balconista"
}

#exibindo o valor associado a uma chave específica
print(dicionario["R2-D2"],"\n")

#None para o que não está no dicionario
print(dicionario.get("Victor"),"\n")

#Mostra os valores
print(dicionario.keys(),"\n")

#exibindo todos os valores em um dicionario
for valor in dicionario.values():
    print(valor,)

#Quantos itens tem no dicionario
print("\n", len(dicionario.values()), "\n")

#Existe sith no dicionari?
print("Sith" in dicionario.values(), "\n")

#itens do dicionario dentro de uma tupla
print(dicionario.items(), "\n")

#uma tupla em cada volta nesse looping
for item in dicionario.items():
    print(item)

print("\n")

#desempacotando
for nome, categoria in dicionario.items():
    print(f"O personagem {nome} é um {categoria}")