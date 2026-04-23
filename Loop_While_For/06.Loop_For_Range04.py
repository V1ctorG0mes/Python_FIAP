for dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:
    dia = input("Digite que dia é hoje: ")
    if dia == "segunda" or dia == "quarta" or dia == "sexta":
        print("É dia de colocar o lixo para o coletor de lixo")
    else:
        print("Não é dia de coleta de lixo")