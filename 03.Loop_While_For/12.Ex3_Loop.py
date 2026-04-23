numero_usuario = int(input("Digite um valor numérico inteiro: "))

anterior1 = 1
anterior2 = 0

#fibonnaci (0, 1, 1, 2, 3, 5, 8...)
for n_elemento in range(1, numero_usuario + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero_usuario == atual:
        print("Ação bem sucedida")
        break
    elif numero_usuario < atual:
        print("Ação falhou")
        break