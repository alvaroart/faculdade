#lista = [ 2, 4, 8, 0, 3, 0, 15, 12, 3, 2]
#exercicio tutoria moda

lista = [ 10, 19, 7, 6, 19, 7, 8, 10, 7, 12]

#frequencia = [nome] * 10
frequencia = [0] * len(lista)

#frequencia = [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0]

for i in range(len(lista)):
  pivo = lista [i]
  cont=1
  
  for j in range (i+1, (len (lista))):
    if pivo == lista[j]:
      cont +=1
  frequencia[i] = cont

maior = 1
for i in range(1,10):
  if frequencia[maior] < frequencia[i]:
    maior = i


print (frequencia)
print ("\t\nA moda é:", lista[maior])
