#valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5, 3.5]

#exibição da lista
print("A lista foi criada assim: {}".format(valores))

#contagem de elementos 1
contagem = valores.count(1)
print(f"\nA contagem de números 1 foi de {contagem}")

#Invertendo a lista
valores.reverse()
print(f"\nA lista invertida ficou assim: {valores}")

#Ordenando a lista
valores.sort() #valores.sort(reverse=True)
print(f"\nA lista em ordem crescente ficou assim: {valores}")

#Tamanho da lista
quantidade = len(valores)
print(f"\nA quantidade de elementos na lista é {quantidade}")

#Soma dos elementos
soma = sum(valores)
print(f"\nA soma dos valores é {soma}")
