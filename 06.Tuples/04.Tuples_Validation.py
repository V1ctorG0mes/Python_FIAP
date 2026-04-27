categorias = ("A", "B", "C", "D", "E")

categoria = (input("Digite a categoria de sua CNH: "))

if categoria in categorias:
    print("Categoria existente!")
else:
    print("Categoria inexistente")