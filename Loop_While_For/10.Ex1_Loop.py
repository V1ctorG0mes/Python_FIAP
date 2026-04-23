quant_alimentos = int(input("Quantos alimentos você comeu hoje? "))
total_calorias = 0

for alimento in range(1, quant_alimentos + 1, 1):
    caloria = int(input("informe a quantida de calorias do {} alimento: ".format(alimento)))
    total_calorias = total_calorias + caloria

print("Foram consumidas {} calorias ao longo do dia".format(total_calorias))