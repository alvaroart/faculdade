#Imprimir os numeros pares entre 0 e um numero foenrcido usando if

fim = int(input ("Digite o numero final: "))
x = 1
while x <= fim:
	if x%2 == 0:
		print (x)
	x = x + 1