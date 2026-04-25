#Função que calcula a velocidade média
def calcularVelocidadeMedia():
    #solicitar distância e tempo
    distancia = float(input("Digite a distância percorrida: "))
    tempo = float(input("Digite o tempo da viagem: "))
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {:.2f} km/h".format(velocidade_media))

#aqui começa o programa principal
calcularVelocidadeMedia()