#lista com 100 elementos aleatorios no interbvalo de 0 a 40. Remova da lista os valores duplicados
#e mostre seu conteudo.

#sub programas
def preencher (listaElemens, qtd, min, max):
    from random import randint
    for item in range (qtd):
        listaElemens.append(randint(min,max))
    return None
def removerDuplicatas (elems):
    indice = 0
    while indice<len(elems):
        if elems.count(elems[indice]) == 1:
            indice +=1
        else:
            elems.remove(elems[indice])
    return None
#programa principal
numeros = []
preencher(numeros,100,0,40)
print(numeros)
removerDuplicatas(numeros)
print("\nSem duplicata: ",numeros)