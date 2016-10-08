#sub programas
def preencher (listaElemens, qtd, min, max):
    from random import randint
    for item in range (qtd):
        listaElemens.append(randint(min,max))
    return None
#programa principal
qtdNumeros = int(input("A lista deve ter quantos valores?"))
minimo = int(input("Menor valor da lista: "))
maximo = int(input("Maior Valor da lista: "))
numeros = []
preencher(numeros,qtdNumeros,minimo,maximo)
print(numeros)