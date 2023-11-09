limite = int(input(f"digite o limite: "))
lista = []
for numeros in range(limite, 0,-1):
    lista.insert(limite, numeros)
print(lista)