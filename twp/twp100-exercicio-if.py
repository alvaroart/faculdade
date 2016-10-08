#Pergunte a velocidade de um carro, supondo um valor inteiro.
#Caso ultrapasse 110 km/hora, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 110.

velocidade = int(input("\n\tDigite a velocidade: "))
if velocidade <= 110:
    print("\n\tParabens, vc esta no limite!")
if velocidade > 110:
    multa = (velocidade - 110) * 5
    #print("\n\tVc foi multado em", multa, "reais.")
    print("Valor multa: R$ %5.2f" %multa)