minutos = int(input("lnforme o número dos minutos do horário atual "))
fatorial = minutos

for numero in range(1, minutos):
    fatorial = fatorial * numero

print (f"A senha é LIBERDADE{fatorial}")