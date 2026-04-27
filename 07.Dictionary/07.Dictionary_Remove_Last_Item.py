#criando um dicionario com dados
dicionario = {
    "Yoda":"Mestre Jedi",
    "Mace Windu": "Mestre Jedi",
    "Anakin Skywalker":"Cavaleiro Jedi",
    "R2-D2":"Dróide",
    "Dex":"Balconista"
}

#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

#removendo o último item
dicionario.popitem()

print("\n")

#exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))