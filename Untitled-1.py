nm=input("informe o nome do atleta: ")
lista=[]
soma=0
for i in range(1,6):
    st=float(input(f"informe o {i} salto: "))
    soma=st+soma
    lista.append(st)
    media=soma/5
print(f"nome = {nm}")
print(f"saltos = {lista}")
print(f"a media dos saltos: {media}m")