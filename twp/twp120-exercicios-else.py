
minutos= int(input("Minutos utilizados: "))
if minutos < 200:
    conta = 0.20
else:
    if minutos <= 400:
        conta=0.18
    else:
        conta = 0.15
print("conta: R$ %6.2f" %(minutos*conta))